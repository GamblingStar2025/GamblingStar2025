
import streamlit as st
import random

st.title("🎰 Monaco-Casino-Strategie")

st.markdown("""
Diese Strategie simuliert ein „Lotto-Slot-Machine“-Feeling. Per Klick generierst du einen zufälligen Tipp,
basierend auf einem gewichteten Zufallssystem – wie im Casino.
""")

if st.button("🎲 Zufällige Zahlen generieren"):
    zahlen = random.sample(range(1, 51), 5)
    lucky_stars = random.sample(range(1, 13), 2)
    st.success(f"🎰 Ihre Monaco-Ziehung: {sorted(zahlen)} + Sterne: {sorted(lucky_stars)}")
