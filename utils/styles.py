APP_STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* 1. Reset e Fundo Suave (Zero cansaço visual) */
    html, body, [class*="css"], .stApp {
        background-color: #F8FAFC !important;
        color: #1E293B !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Esconde elementos nativos desnecessários do Streamlit */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* 2. Container Centralizado com Boa Proporção */
    .block-container {
        max-width: 640px !important;
        padding-top: 3.5rem !important;
        padding-bottom: 3.5rem !important;
    }

    /* 3. Tipografia Elegante */
    .app-title {
        font-size: 1.85rem !important;
        font-weight: 700 !important;
        color: #0F172A !important;
        text-align: center;
        letter-spacing: -0.025em;
        margin-bottom: 0.4rem;
    }

    .app-subtitle {
        font-size: 0.95rem !important;
        color: #64748B !important;
        text-align: center;
        margin-bottom: 2.5rem;
    }

    /* 4. Área de Upload Refinada (Estilo Cartão Flutuante) */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.2s ease;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: #CBD5E1 !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.04) !important;
    }

    [data-testid="stFileUploader"] section {
        background-color: transparent !important;
    }

    [data-testid="stFileUploader"] span, 
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] p {
        color: #475569 !important;
    }

    /* 5. Seletor de Idioma Discreto e Limpo */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        color: #1E293B !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.02);
    }

    /* 6. Botão Principal (Verde Esmeralda Profissional - Referência ao Excel) */
    div.stButton > button[kind="primary"],
    div.stDownloadButton > button[kind="primary"] {
        background-color: #059669 !important; /* Esmeralda elegante */
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2) !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="primary"]:hover,
    div.stDownloadButton > button[kind="primary"]:hover {
        background-color: #047857 !important;
        box-shadow: 0 6px 16px rgba(5, 150, 105, 0.3) !important;
        transform: translateY(-1px);
    }

    /* Botão Secundário */
    div.stButton > button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #475569 !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 12px !important;
        padding: 0.65rem 1.25rem !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="secondary"]:hover {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        border-color: #94A3B8 !important;
    }

    /* 7. Card de Sucesso Limpo */
    .status-card {
        background-color: #FFFFFF !important;
        border: 1px solid #BBF7D0 !important;
        border-left: 4px solid #10B981 !important;
        border-radius: 12px !important;
        padding: 1.25rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02) !important;
        margin-bottom: 1.5rem !important;
    }

    /* Card de Cabeçalho Moderno (Substitui a barra feia) */
    .app-header-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 1.25rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02) !important;
        margin-bottom: 1.5rem !important;
    }

    .header-icon-box {
        background-color: #ECFDF5 !important;
        width: 52px !important;
        height: 52px !important;
        border-radius: 14px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        flex-shrink: 0 !important;
    }

    .header-text-content {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important; /* Garante alinhamento total à esquerda */
        text-align: left !important;
    }

    .app-title {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: #0F172A !important;
        margin: 0 !important;
        letter-spacing: -0.02em !important;
        text-align: left !important;
    }

    .app-subtitle {
        font-size: 0.875rem !important;
        color: #64748B !important;
        margin: 0.25rem 0 0 0 !important;
        text-align: left !important;
    }
</style>
"""