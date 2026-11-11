
import streamlit as st

st.set_page_config(
    page_title="Westy Wackers",
    page_icon="⛳",
    layout="wide"
)

st.title("⛳ Westy Wackers")
st.subheader("Golf Competition Dashboard")

st.info("Welcome to the Westy Wackers Golf Dashboard!")

tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Ladders",
    "👥 Players",
    "📊 Statistics",
    "🔐 Admin"
])

with tab1:
    st.header("Competition Ladders")
    st.write("Ladders will appear here.")

with tab2:
    st.header("Players")
    st.write("Player profiles will appear here.")

with tab3:
    st.header("Statistics")
    st.write("Golf statistics will appear here.")

with tab4:
    st.header("Administration")
    st.warning("Admin login has not been configured yet.")
