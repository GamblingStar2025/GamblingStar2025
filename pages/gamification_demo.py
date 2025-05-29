import streamlit as st

st.title("🎮 Gamification-Demo")

punkte = st.slider("Wähle deine Glückszahl", 0, 100)

if punkte > 70:
    st.success("Du hast ein Highscore erreicht! 🥳")
else:
    st.info("Versuch's noch einmal! 🎲")
