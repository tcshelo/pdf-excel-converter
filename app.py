import streamlit as st
from utils.converter import convert_pdf_to_excel
from utils.translations import TRANSLATIONS
from utils.styles import APP_STYLES

# 1. Configuração da página (DEVE ser a primeira chamada do Streamlit)
st.set_page_config(
    page_title="Conversor PDF para Excel / PDF to Excel Converter",
    page_icon="📊",
    layout="centered"
)

# 2. Aplica os estilos CSS externos
st.markdown(APP_STYLES, unsafe_allow_html=True)

# 3. Seletor de Idioma no topo da página (à direita)
col1, col2 = st.columns([4, 1])
with col2:
    selected_lang = st.selectbox(
        "Language", 
        options=["PT-BR", "EN"],
        index=0,
        label_visibility="collapsed"
    )

# 4. Define a chave ativa e carrega as traduções
lang_key = "PT" if selected_lang == "PT-BR" else "EN"
t = TRANSLATIONS[lang_key]

# 5. Exibe o Cabeçalho Único Estilizado
st.markdown(f"""
    <div class="app-header-card">
        <div class="header-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
        </div>
        <div class="header-text-content">
            <h1 class="app-title">{t["title"]}</h1>
            <p class="app-subtitle">{t["subtitle"]}</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Função para resetar completamente a aplicação para uma nova tentativa
def reset_application():
    st.session_state['success_status'] = False
    st.session_state['error_message'] = None
    st.session_state.pop('excel_bytes', None)
    st.session_state.pop('output_filename', None)
    st.session_state['uploader_key'] = st.session_state.get('uploader_key', 0) + 1

# Inicializa as variáveis de sessão caso não existam
if 'uploader_key' not in st.session_state:
    st.session_state['uploader_key'] = 0
if 'error_message' not in st.session_state:
    st.session_state['error_message'] = None

# Fluxo 1: Se a conversão JÁ FOI CONCLUÍDA com sucesso
if st.session_state.get('success_status', False):
    st.markdown(f"""
        <div class="status-card">
            <span style="color: #166534; font-weight: 600; font-size: 1.05rem;">{t['success_title']}</span>
            <p style="color: #64748B; font-size: 0.85rem; margin-top: 0.3rem; margin-bottom: 0;">{t['success_desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.download_button(
        label=t["download_btn"],
        data=st.session_state['excel_bytes'],
        file_name=st.session_state['output_filename'],
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
        use_container_width=True
    )
    
    st.write("")
    
    if st.button(t.get("reset_btn", "Converter outro arquivo"), type="secondary", use_container_width=True):
        reset_application()
        st.rerun()

# Fluxo 2: Se OCORREU UM ERRO na conversão (some o botão de converter e exibe o alerta com opção de tentar de novo)
elif st.session_state.get('error_message') is not None:
    st.error(f"⚠️ {st.session_state['error_message']}")
    st.write("")
    if st.button(t.get("reset_btn", "Tentar outro arquivo"), type="primary", use_container_width=True):
        reset_application()
        st.rerun()

# Fluxo 3: Estado padrão (Aguardando upload e com o botão de converter habilitado)
else:
    pdf_upload = st.file_uploader(
        t["uploader_label"], 
        type=["pdf"],
        help=t["uploader_help"],
        key=f"pdf_uploader_{st.session_state['uploader_key']}"
    )

    if pdf_upload is not None:
        st.caption(f"{t['selected_file']} **{pdf_upload.name}**")
        
        if st.button(t["convert_btn"], type="primary", use_container_width=True):
            try:
                with st.spinner(t["spinner"]):
                    excel_bytes = convert_pdf_to_excel(pdf_upload, lang=lang_key)
                    output_filename = pdf_upload.name.replace(".pdf", ".xlsx")
                    
                    st.session_state['excel_bytes'] = excel_bytes
                    st.session_state['output_filename'] = output_filename
                    st.session_state['success_status'] = True
                    st.session_state['error_message'] = None
                    st.rerun()
                    
            except ValueError as error:
                st.session_state['error_message'] = str(error)
                st.rerun()
            except RuntimeError as error:
                st.session_state['error_message'] = str(error)
                st.rerun()
            except Exception as error:
                st.session_state['error_message'] = f"Erro inesperado / Unexpected error: {error}"
                st.rerun()