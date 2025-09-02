import streamlit as st
from datetime import datetime

# =========================
# Config & Tema
# =========================
st.set_page_config(
    page_title="Hello Streamlit Pro",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    :root {
    --gap: 0.8rem;
    }
    .block-container {padding-top: 1.5rem;}
    .metric-card {border: 1px solid #e6e6e6; border-radius: 12px; padding: 1rem;}
    .section {margin-top: 1.2rem;}
    .small {font-size: 0.9rem; color: #666;}
    </style>
    """, 
    unsafe_allow_html=True
)

# =========================
# Helpers de UI
# =========================
def metric_card(label: str, value: str | float, help_text: str = ""):
    col = st.container()
    with col:
        st.markdown(f"<div class='metric-card'><h4>{label}</h4><h2>{value}</h2>"
                    f"<div class='small'>{help_text}</div></div>", unsafe_allow_html=True)


# =========================
# Estado Global
# =========================
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.header("Configurações")
    username = st.text_input("Seu nome", value="Yago")
    theme = st.radio("Tema", ["Claro", "Escuro"], index=0)
    show_data = st.toggle("Mostrar dados de exemplo", value=True)
    st.write("---")
    st.write("Sessões nesta execução:", st.session_state.visits)

# =========================
# Header
# =========================
st.title("👋 Hello, Streamlit Pro")
st.caption("Layout base + estado + componentes reutilizáveis.")

# =========================
# KPIs
# =========================
c1, c2, c3, c4 = st.columns(4)
with c1: metric_card("Usuário", username, "Nome ativo")
with c2: metric_card("Tema", theme, "Preferência visual")
with c3: metric_card("Visitas (sessão)", st.session_state.visits, "Incrementa a cada reload")
with c4: metric_card("Agora", datetime.now().strftime("%H:%M:%S"), "Horário local")
