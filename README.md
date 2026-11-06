# 📄 Conversor de PDF para Excel / PDF to Excel Converter

[Português](#português) | [English](#english)

---

<a name="português"></a>
## 🇧🇷 Português

Aplicação moderna desenvolvida em **Python** e **Streamlit** para extrair tabelas de arquivos PDF e convertê-las em planilhas do Excel (`.xlsx`) limpas e formatadas.

### ✨ Funcionalidades

- **Extração Inteligente:** Processa tabelas a partir de texto selecionável em PDF utilizando o `pdfplumber`.
- **Tratamento de Células Mescladas:** Identifica e unifica blocos horizontais (como cabeçalhos de seções) aplicando o `merge_range` real no Excel.
- **Suporte Bilíngue (i18n):** Alternância fluida entre Português e Inglês diretamente na interface.
- **Design Corporativo & Minimalista:** Formatação profissional automática com cabeçalhos estilizados, ajuste de colunas, card de cabeçalho dedicado e tema limpo.
- **Fluxo de Erros Resiliente:** Tratamento inteligente de falhas com ocultação automática de botões inválidos e botão dinâmico para novas conversões.

### 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Streamlit** (Interface gráfica reativa)
- **Pandas** (Manipulação e estruturação de dados)
- **Pdfplumber** (Extração avançada de tabelas de PDF)
- **XlsxWriter** (Geração e estilização de planilhas)

---

<a name="english"></a>
## 🇺🇸 English

A modern application built with **Python** and **Streamlit** to extract tables from PDF files and convert them into clean and formatted Excel spreadsheets (`.xlsx`).

### ✨ Features

- **Smart Extraction:** Processes tables from selectable text in PDF files using `pdfplumber`.
- **Merged Cell Support:** Detects and unifies horizontal blocks using native Excel `merge_range` to prevent duplicate values.
- **Bilingual Support (i18n):** Seamless language switching between Portuguese and English directly on the interface.
- **Corporate & Minimalist Design:** Professional auto-styling, clean typography, dedicated header card, and optimized layout.
- **Resilient Error Handling:** Intelligent failure recovery with dynamic state management and instant retry options.

### 🛠️ Built With

- **Python 3.11+**
- **Streamlit** (Reactive User Interface)
- **Pandas** (Data manipulation and structuring)
- **Pdfplumber** (PDF table extraction)
- **XlsxWriter** (Advanced Excel file generation and styling)
