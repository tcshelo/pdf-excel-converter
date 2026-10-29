import pdfplumber
import pandas as pd
import io

def convert_pdf_to_excel(pdf_file, lang="PT"):
    """
    Processa um arquivo PDF buscando tabelas, identifica células mescladas horizontais
    reais para aplicar o merge no Excel e exporta formatado em cinza escuro.
    """
    try:
        all_data = []
        
        # Abre o arquivo PDF com pdfplumber
        with pdfplumber.open(pdf_file) as pdf:
            if not pdf.pages:
                if lang == "EN":
                    raise ValueError("The PDF file is empty or has no readable pages.")
                else:
                    raise ValueError("O arquivo PDF está vazio ou não possui páginas legíveis.")
            
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    all_data.extend(table)
                    
        if not all_data:
            if lang == "EN":
                raise ValueError("No structured tables were identified in this PDF. Make sure the document contains tables in selectable text and not scanned images.")
            else:
                raise ValueError("Nenhuma tabela estruturada foi identificada neste PDF. Certifique-se de que o documento contém tabelas em texto selecionável e não imagens escaneadas.")
            
        # Converte os dados brutos em DataFrame
        df = pd.DataFrame(all_data)
        
        # Tratamento rigoroso de nulos para análise de spans
        df = df.replace(r'^\s*$', pd.NA, regex=True)
        df = df.replace(["nan", "NaN", "None", ""], pd.NA)
        
        # Remove quebras de página repetidas se houver cabeçalhos duplicados
        if len(df) > 2:
            header_signature = df.iloc[1].tolist()
            mask = ~df.iloc[2:].astype(str).eq([str(c) for c in header_signature]).all(axis=1)
            df = pd.concat([df.iloc[:2], df.iloc[2:][mask]]).reset_index(drop=True)
            
        # Sanitiza dados para evitar injeção de fórmulas no Excel
        for col in df.columns:
            df[col] = df[col].apply(
                lambda x: f"'{x}" if isinstance(x, str) and x.startswith('=') else x
            )

        # Salva os dados usando XlsxWriter com mesclagem real e cinza escuro
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, header=False, sheet_name='Relatório' if lang == "PT" else 'Report')
            
            workbook = writer.book
            worksheet = writer.sheets['Relatório' if lang == "PT" else 'Report']
            
            # Formato Cinza Escuro Elegante (Slate 700) para o Cabeçalho Principal
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'fg_color': '#334155',
                'font_color': '#FFFFFF',
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'border_color': '#1E293B'
            })
            
            # Formato para o Sub-cabeçalho
            sub_header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'fg_color': '#475569',
                'font_color': '#FFFFFF',
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'border_color': '#1E293B'
            })
            
            # Formato Padrão para as Células de Dados
            cell_format = workbook.add_format({
                'text_wrap': True,
                'valign': 'top',
                'border': 1,
                'border_color': '#E2E8F0'
            })
            
            # 1. Processa a Linha 0 (Nomes mesclados horizontalmente)
            if len(df) > 0:
                row_zero = df.iloc[0].tolist()
                spans = []
                start_col = 0
                current_val = row_zero[0] if len(row_zero) > 0 else None
                
                for col_idx in range(1, len(row_zero)):
                    val = row_zero[col_idx]
                    if pd.isna(val):
                        continue
                    else:
                        spans.append((start_col, col_idx - 1, current_val))
                        start_col = col_idx
                        current_val = val
                if len(row_zero) > 0:
                    spans.append((start_col, len(row_zero) - 1, current_val))
                    
                for start_col, end_col, val in spans:
                    val_str = "" if pd.isna(val) else str(val)
                    if start_col == end_col:
                        worksheet.write(0, start_col, val_str, header_format)
                    else:
                        worksheet.merge_range(0, start_col, 0, end_col, val_str, header_format)
            
            # 2. Processa a Linha 1 (Sub-cabeçalho das colunas)
            if len(df) > 1:
                for col_idx in range(len(df.columns)):
                    val = df.iloc[1, col_idx]
                    val_str = "" if pd.isna(val) else str(val)
                    worksheet.write(1, col_idx, val_str, sub_header_format)
            
            # 3. Processa o restante das linhas (Dados)
            header_rows_count = 2 if len(df) >= 2 else 1
            for row_idx in range(header_rows_count, len(df)):
                for col_idx in range(len(df.columns)):
                    val = df.iloc[row_idx, col_idx]
                    val_str = "" if pd.isna(val) else str(val)
                    worksheet.write(row_idx, col_idx, val_str, cell_format)

            # Ajusta automaticamente a largura das colunas
            for i in range(len(df.columns)):
                max_len = 0
                for row_idx in range(len(df)):
                    cell_val = df.iloc[row_idx, i]
                    if pd.notna(cell_val):
                        max_len = max(max_len, len(str(cell_val)))
                worksheet.set_column(i, i, max(max_len + 4, 15))
                
        return output.getvalue()

    except ValueError as error:
        raise error
    except Exception as error:
        error_message = str(error).lower()
        if "syntax" in error_message or "pdf" in error_message or "format" in error_message:
            if lang == "EN":
                raise ValueError("The PDF file is corrupted, damaged, or has an invalid format.")
            else:
                raise ValueError("O arquivo PDF está corrompido, danificado ou com formato inválido.")
        
        if lang == "EN":
            raise RuntimeError(f"An internal error occurred while processing the file: {str(error)}")
        else:
            raise RuntimeError(f"Ocorreu um erro interno ao processar o arquivo: {str(error)}")