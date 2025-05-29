import streamlit as st
from supabase_connector import supabase

st.set_page_config(page_title="🧠 Strategien", layout="centered")
st.title("🧠 Letzte KI-Tipps")

email = st.session_state.get("user_email", "gast@demo.com")

try:
    daten = supabase.table("strategien").select("*").eq("email", email).order("created_at", desc=True).limit(10).execute()
    eintraege = daten.data if hasattr(daten, 'data') else daten

    if not eintraege:
        st.info("ℹ️ Noch keine Strategien gespeichert.")
    else:
        for eintrag in eintraege:
            st.subheader(f"📌 {eintrag['name']}")
            param = eintrag.get("parameter", {})
            zahlen = param.get("tipp") or param.get("tipps") or param
            st.code(zahlen, language="json")
except Exception as e:
    st.error(f"❌ Fehler beim Laden der Strategien: {e}")
