
import streamlit as st
import time
from PIL import Image

st.set_page_config(page_title="EuroGenius Start", layout="centered", initial_sidebar_state="collapsed")

page_style = '''
<style>
body {
    background-color: #0c0c0c;
    color: #f1f1f1;
    text-align: center;
}
img {
    max-width: 250px;
    margin-top: 50px;
}
h1 {
    font-size: 2.5rem;
    margin-top: 1rem;
    color: gold;
}
</style>
'''
st.markdown(page_style, unsafe_allow_html=True)

# Lade Logo über PIL
try:
    logo = Image.open("logo_gold.png")
    st.image(logo, use_container_width=False)
except:
    st.warning("Logo konnte nicht geladen werden.")

st.markdown("## EuroGenius – KI trifft auf Glück ✨")

with st.spinner("App wird vorbereitet..."):
    time.sleep(2)

if st.button("➡️ Jetzt starten"):
    st.switch_page("main_app")
