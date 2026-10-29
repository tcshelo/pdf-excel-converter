# 📊 Conversor de PDF para Excel / PDF to Excel Converter

[Português](#português) | [English](#english)

---

<a name="português"></a>
## 🇧🇷 Português

Aplicação desktop moderna desenvolvida em **Python** e **Streamlit** para extrair tabelas de arquivos PDF e convertê-las em planilhas do Excel (`.xlsx`) limpas e formatadas.

### ✨ Funcionalidades

- **Extração Inteligente:** Processa tabelas a partir de texto selecionável em PDF utilizando o `pdfplumber`.
- **Tratamento de Células Mescladas:** Identifica e unifica blocos horizontais (como cabeçalhos de seções ou grupos) aplicando o `merge_range` real no Excel para evitar valores duplicados ou `NaN`.
- **Design Corporativo:** Formatação profissional automática com cabeçalhos em cinza escuro (`#334155`), texto em branco, margens e ajuste automático da largura das colunas.
- **Interface Estilo Desktop:** Layout minimalista focado na produtividade, ocultando elementos web padrão e gerenciando estados de forma fluida.
- **Fluxo de Reinicialização:** Botão dinâmico para efetuar novas conversões com um único clique.

### 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Streamlit** (Interface gráfica)
- **Pandas** (Manipulação e estruturação de dados)
- **Pdfplumber** (Extração de tabelas de PDF)
- **XlsxWriter** (Geração e estilização avançada de arquivos Excel)

---

<a name="english"></a>
## 🇺🇸 English

A modern desktop application built with **Python** and **Streamlit** to extract tables from PDF files and convert them into clean and formatted Excel spreadsheets (`.xlsx`).

### ✨ Features

- **Smart Extraction:** Processes tables from selectable text in PDF files using `pdfplumber`.
- **Merged Cell Support:** Detects and unifies horizontal blocks (such as section or group headers) using native Excel `merge_range` to prevent duplicate values or `NaN` entries.
- **Corporate Design:** Automatic professional styling with dark gray headers (`#334155`), white text, grid lines, and auto-adjusted column widths.
- **Desktop-Style UI:** Minimalist layout built for productivity, hiding standard web elements and managing application state seamlessly.
- **Reset Workflow:** Dynamic button to start a new conversion in a single click.

### 🛠️ Built With

- **Python 3.11+**
- **Streamlit** (User Interface)
- **Pandas** (Data manipulation and structuring)
- **Pdfplumber** (PDF table extraction)
- **XlsxWriter** (Advanced Excel file generation and styling)
