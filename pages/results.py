
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Deine Tipps", layout="centered")
st.title("🎫 Ergebnis: Deine Tipps")

if "tipps" not in st.session_state:
    st.warning("⚠️ Keine Tipps vorhanden.")
    st.stop()

tipps = st.session_state.tipps
df_out = pd.DataFrame([{"Tipp": i+1, "Zahlen": t[0], "Sterne": t[1]} for i, t in enumerate(tipps)])
st.dataframe(df_out)

csv = df_out.to_csv(index=False).encode("utf-8")
st.download_button("📥 Tipps herunterladen", data=csv, file_name="eurogenius_tipps.csv", mime="text/csv")

if st.button("🔁 Neue Analyse starten"):
    st.switch_page("main")
