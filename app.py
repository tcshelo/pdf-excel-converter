# app.py
import streamlit as st
import base64
import streamlit.components.v1 as components
from utils.converter import convert_pdf_to_excel

# Configuração da página para estilo janela de aplicativo
st.set_page_config(
    page_title="Conversor PDF para Excel",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS customizada para aparência de Software Desktop limpa
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 650px;
    }
    
    .app-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.25rem;
        text-align: center;
    }
    
    .app-subtitle {
        font-size: 0.875rem;
        color: #64748B;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .status-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.25rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .backup-link-container {
        text-align: center;
        margin-top: 0.75rem;
        margin-bottom: 1.5rem;
    }
    
    .backup-link {
        font-size: 0.85rem;
        color: #64748B;
        text-decoration: underline;
    }
    
    .backup-link:hover {
        color: #0F172A;
    }
    </style>
""", unsafe_allow_html=True)

# Função para resetar completamente a aplicação para uma nova conversão
def reset_application():
    st.session_state['success_status'] = False
    st.session_state.pop('excel_bytes', None)
    st.session_state.pop('output_filename', None)
    st.session_state['uploader_key'] = st.session_state.get('uploader_key', 0) + 1

# Inicializa as variáveis de sessão caso não existam
if 'uploader_key' not in st.session_state:
    st.session_state['uploader_key'] = 0

# Conteúdo Principal
st.markdown('<div class="app-title">📊 Conversor de PDF para Excel</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Selecione o relatório em PDF para gerar a planilha formatada</div>', unsafe_allow_html=True)

# Se a conversão AINDA NÃO foi feita, exibe o fluxo de Upload e o Botão "Converter"
if not st.session_state.get('success_status', False):
    pdf_upload = st.file_uploader(
        "Arraste ou selecione o arquivo PDF", 
        type=["pdf"],
        help="Selecione um arquivo PDF que contenha tabelas.",
        key=f"pdf_uploader_{st.session_state['uploader_key']}"
    )

    if pdf_upload is not None:
        st.caption(f"📁 Arquivo selecionado: **{pdf_upload.name}**")
        
        if st.button("⚡ Converter para Excel", type="primary", use_container_width=True):
            try:
                with st.spinner("Processando dados do PDF..."):
                    excel_bytes = convert_pdf_to_excel(pdf_upload)
                    output_filename = pdf_upload.name.replace(".pdf", ".xlsx")
                    
                    st.session_state['excel_bytes'] = excel_bytes
                    st.session_state['output_filename'] = output_filename
                    st.session_state['success_status'] = True
                    st.rerun()
                    
            except ValueError as error:
                st.error(f"⚠️ {error}")
            except RuntimeError as error:
                st.error(f"❌ {error}")
            except Exception as error:
                st.error(f"Erro inesperado: {error}")

# Se a conversão JÁ FOI CONCLUÍDA
else:
    b64_data = base64.b64encode(st.session_state['excel_bytes']).decode()
    filename = st.session_state['output_filename']
    
    # Injeção segura via string concatenation em JavaScript puro (sem conflito de chaves do Python)
    download_script = f"""
        <script>
            var b64Data = "{b64_data}";
            var fileName = "{filename}";
            
            function b64toBlob(b64Data, contentType) {{
                contentType = contentType || '';
                var byteCharacters = atob(b64Data);
                var byteArrays = [];
                for (var offset = 0; offset < byteCharacters.length; offset += 512) {{
                    var slice = byteCharacters.slice(offset, offset + 512);
                    var byteNumbers = new Array(slice.length);
                    for (var i = 0; i < slice.length; i++) {{
                        byteNumbers[i] = slice.charCodeAt(i);
                    }}
                    var byteArray = new Uint8Array(byteNumbers);
                    byteArrays.push(byteArray);
                }}
                return new Blob(byteArrays, {{type: contentType}});
            }}
            
            var blob = b64toBlob(b64Data, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            var blobUrl = URL.createObjectURL(blob);
            
            var a = document.createElement("a");
            a.href = blobUrl;
            a.download = fileName;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        </script>
    """
    
    components.html(download_script, height=0, width=0)

    st.markdown("""
        <div class="status-card">
            <span style="color: #166534; font-weight: 600; font-size: 1.05rem;">✅ Conversão concluída com sucesso!</span>
            <p style="color: #64748B; font-size: 0.85rem; margin-top: 0.3rem; margin-bottom: 0;">O arquivo foi gerado e o download automático foi disparado.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Fazer Nova Conversão", type="primary", use_container_width=True):
        reset_application()
        st.rerun()

    href = f"data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_data}"
    st.markdown(f"""
        <div class="backup-link-container">
            <a class="backup-link" href="{href}" download="{filename}">O download automático não iniciou? Clique aqui para baixar manualmente.</a>
        </div>
    """, unsafe_allow_html=True)