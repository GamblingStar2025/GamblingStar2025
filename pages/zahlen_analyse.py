import streamlit as st
import matplotlib.pyplot as plt

uploaded_file = st.session_state.get("csv_data", None)

st.title("📊 Zahlenanalyse")

if uploaded_file is not None:
    df = uploaded_file
    zahlen = df.iloc[:, 1:].stack().value_counts()

    fig, ax = plt.subplots()
    zahlen.head(20).sort_index().plot(kind="bar", ax=ax)
    st.pyplot(fig)
else:
    st.warning("Bitte lade eine CSV-Datei über die Seitenleiste hoch.")
