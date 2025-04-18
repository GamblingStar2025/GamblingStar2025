
import streamlit as st
from pages.home import show_home

st.set_page_config(page_title="EuroGenius", layout="centered")

def main():
    show_home()

if __name__ == "__main__":
    main()
