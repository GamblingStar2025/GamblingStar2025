
import streamlit as st
import numpy as np

st.title("🎡 Rad-Prinzip Strategie")

st.markdown("""
Diese Strategie wählt gleichmäßig verteilte Zahlen entlang eines gedachten Zahlenrades.
Das Ziel ist eine balancierte Auswahl aus allen Bereichen.
""")

def rad_verteilung(n=5, bereich=50):
    return [int(i * (bereich / n) + 1) for i in range(n)]

zahlen = rad_verteilung()
lucky_stars = rad_verteilung(2, 12)

st.success(f"🎯 Rad-Auswahl: {zahlen} + Sterne: {lucky_stars}")
