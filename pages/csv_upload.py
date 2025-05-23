
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Upload", layout="centered")
st.title("📤 CSV hochladen")

file = st.file_uploader("Wähle deine EuroMillions CSV", type="csv")

if file:
    try:
        df = pd.read_csv(file)
        st.session_state.df = df
        st.session_state.csv_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success("CSV erfolgreich gespeichert.")
        st.dataframe(df.tail())

        if st.button("➡️ Weiter zur Konfiguration"):
            st.switch_page("pages/super_prediction.py")
    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")
