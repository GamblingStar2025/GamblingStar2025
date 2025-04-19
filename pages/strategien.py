import streamlit as st
tabs = st.tabs(["🔥 Heiße Zahlen", "❄️ Kalte Zahlen", "🎡 Rad-Prinzip", "🧠 KI", "🎰 Monaco", "🔀 Mischer"])
with tabs[0]:
    st.write("Strategie: Heiße Zahlen")
with tabs[1]:
    st.write("Strategie: Kalte Zahlen")
with tabs[2]:
    st.write("Strategie: Rad-Prinzip")
with tabs[3]:
    st.write("Strategie: KI Analyse")
with tabs[4]:
    st.write("Strategie: Monaco Simulation")
with tabs[5]:
    st.write("Strategie: Kombinationen")
