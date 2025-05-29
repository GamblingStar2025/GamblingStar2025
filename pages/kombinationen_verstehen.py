import streamlit as st
import math

st.title("🧮 Kombinationen verstehen")

st.markdown("""
In EuroMillions wählst du **5 aus 50 Zahlen** und **2 aus 12 Sternen**.

Die Gesamtzahl möglicher Kombinationen ist:

\[
\text{Kombis} = \binom{50}{5} \times \binom{12}{2}
\]

Das ergibt:
""")

kombi_zahlen = math.comb(50, 5)
kombi_sterne = math.comb(12, 2)
gesamt = kombi_zahlen * kombi_sterne

st.latex(f"{kombi_zahlen} \times {kombi_sterne} = {gesamt:,}".replace(",", "'"))
st.success(f"🎯 Insgesamt {gesamt:,} mögliche Kombinationen.")
