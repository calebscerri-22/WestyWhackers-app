
import streamlit as st
import pandas as pd
from supabase import create_client

st.set_page_config(
    page_title="Westie Wackers",
    page_icon="⛳",
    layout="wide"
)

# Connect to Supabase
@st.cache_resource
def get_database():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


# Retrieve players
def get_players():
    response = (
        get_database()
        .table("players")
        .select("id, name, nickname, active")
        .order("name")
        .execute()
    )
    return response.data

# Dashboard
st.title("⛳ Westie Wackers")
st.subheader("Golf Competition Dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Ladders",
    "👥 Players",
    "📊 Statistics",
    "🔐 Admin"
])

with tab1:
    st.header("Competition Ladders")
    st.info("Competition ladders coming soon.")

with tab2:
    st.header("Group Members")

    try:
        players = get_players()
        active_players = [
            p for p in players if p["active"]
        ]

        st.metric(
            "Active Members",
            len(active_players)
        )

        if active_players:
            df = pd.DataFrame(active_players)

            st.dataframe(
                df[["name", "nickname"]],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No players added yet.")

    except Exception as e:
        st.error("Unable to load players.")
        st.exception(e)

with tab3:
    st.header("Player Statistics")
    st.info("Statistics coming soon.")

with tab4:
    st.header("Administration")
    st.warning(
        "Administrator login is not configured yet."
    )
