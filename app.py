import streamlit as st
from utils.converter import convert_pdf_to_excel
from utils.translations import TRANSLATIONS
from utils.styles import APP_STYLES

# Configuração da página
st.set_page_config(
    page_title="Conversor PDF para Excel / PDF to Excel Converter",
    page_icon="📊",
    layout="centered"
)

# Aplica os estilos CSS externos
st.markdown(APP_STYLES, unsafe_allow_html=True)

# Seletor de Idioma posicionado discretamente no topo da página (à direita)
col1, col2 = st.columns([4, 1])
with col2:
    selected_lang = st.selectbox(
        "Language", 
        options=["PT-BR", "EN"],
        index=0,
        label_visibility="collapsed"
    )

# Define a chave ativa com base na escolha do usuário
lang_key = "PT" if selected_lang == "PT-BR" else "EN"
t = TRANSLATIONS[lang_key]

# Função para resetar completamente a aplicação para uma nova conversão
def reset_application():
    st.session_state['success_status'] = False
    st.session_state.pop('excel_bytes', None)
    st.session_state.pop('output_filename', None)
    st.session_state['uploader_key'] = st.session_state.get('uploader_key', 0) + 1

# Inicializa as variáveis de sessão caso não existam
if 'uploader_key' not in st.session_state:
    st.session_state['uploader_key'] = 0

# Conteúdo Principal dinâmico baseado no idioma
st.markdown(f'<div class="app-title">{t["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="app-subtitle">{t["subtitle"]}</div>', unsafe_allow_html=True)

# Se a conversão AINDA NÃO foi feita, exibe o fluxo de Upload e o Botão "Converter"
if not st.session_state.get('success_status', False):
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
                    # Passa o idioma atual para a função de conversão tratar os erros corretamente
                    excel_bytes = convert_pdf_to_excel(pdf_upload, lang=lang_key)
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
                st.error(f"Erro inesperado / Unexpected error: {error}")

# Se a conversão JÁ FOI CONCLUÍDA
else:
    st.markdown(f"""
        <div class="status-card">
            <span style="color: #166534; font-weight: 600; font-size: 1.05rem;">{t['success_title']}</span>
            <p style="color: #64748B; font-size: 0.85rem; margin-top: 0.3rem; margin-bottom: 0;">{t['success_desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Botão de download principal em destaque
    st.download_button(
        label=t["download_btn"],
        data=st.session_state['excel_bytes'],
        file_name=st.session_state['output_filename'],
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
        use_container_width=True
    )
    
    st.write("") # Espaçador
    
    # Botão para iniciar novo processo em evidência logo abaixo
    if st.button(t["reset_btn"], type="secondary", use_container_width=True):
        reset_application()
        st.rerun()