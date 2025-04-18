
import streamlit as st
from custom_style import eurogenius_css
from supabase_connector import supabase

st.set_page_config(page_title="Meine Strategien", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("📚 Gespeicherte Strategien")

if not st.session_state.get("is_logged_in"):
    st.error("⚠️ Du musst eingeloggt sein, um deine Strategien zu sehen.")
    st.stop()

email = st.session_state.get("user_email")

try:
    res = supabase.table("Strategien").select("*").eq("email", email).execute()
    daten = res.data

    if daten:
        for eintrag in daten:
            st.markdown(f"### 💡 {eintrag['strategy_name']}")
            st.json(eintrag['parameters'])
    else:
        st.info("ℹ️ Du hast noch keine Strategien gespeichert.")
except Exception as e:
    st.error(f"❌ Fehler beim Laden der Strategien: {e}")
