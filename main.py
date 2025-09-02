import streamlit as st

# =========================
# Config & Tema
# =========================
st.set_page_config(
    page_title="Hello Streamlit Pro",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)
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