import streamlit as st
import math

st.set_page_config(page_title="🧮 Kombinationen verstehen", layout="centered")
st.title("🧮 Kombinationen verstehen")

st.markdown("""
In **EuroMillions** wählst du **5 aus 50 Zahlen** und **2 aus 12 Sternen**.

Die Gesamtzahl möglicher Kombinationen ergibt sich aus der Formel:

\[
\text{Kombis} = \binom{50}{5} \times \binom{12}{2}
\]

Das ergibt:
\[
\binom{50}{5} = 2\,118\,760 \quad \text{und} \quad \binom{12}{2} = 66
\]

\[
\text{Gesamt: } 2\,118\,760 \times 66 = 139\,838\,160 \text{ mögliche Kombinationen}
\]
""")

st.success("🎯 Insgesamt **139,838,160** mögliche Kombinationen.")
