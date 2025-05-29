
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🔍 Zahlenanalyse", layout="wide")
st.title("🔍 Analyse der Zahlenmuster")

uploaded_file = st.file_uploader("📄 Ziehungsdaten (CSV)", type="csv")

def gruppen_analyse(df):
    gruppen = {"hoch": [], "niedrig": [], "gerade": [], "ungerade": []}

    for index, row in df.iterrows():
        zahlen = row[1:6].astype(int)
        gruppen["hoch"].append(sum(z > 25 for z in zahlen))
        gruppen["niedrig"].append(sum(z <= 25 for z in zahlen))
        gruppen["gerade"].append(sum(z % 2 == 0 for z in zahlen))
        gruppen["ungerade"].append(sum(z % 2 != 0 for z in zahlen))

    return pd.DataFrame(gruppen)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.shape[1] >= 6:
        analyse = gruppen_analyse(df)

        st.subheader("📊 Hoch/Tief-Verteilung")
        st.bar_chart(analyse[["hoch", "niedrig"]])

        st.subheader("📊 Gerade/Ungerade-Verteilung")
        st.bar_chart(analyse[["gerade", "ungerade"]])

        st.success("✅ Analyse abgeschlossen")
    else:
        st.error("⚠️ CSV-Format ungültig. Es müssen mindestens 5 Zahlen pro Ziehung enthalten sein.")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
