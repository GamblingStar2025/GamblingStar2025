# Navigation logic for the app
import streamlit as st

def navigate():
    st.sidebar.title("📊 Navigation")
    page = st.sidebar.radio("Gehe zu:", ["Dashboard", "CSV Upload", "Strategien", "Tipp Generator"])
    if page == "Dashboard":
        from pages import dashboard
        dashboard.show()
    elif page == "CSV Upload":
        from pages import csv_upload
        csv_upload.show()
    elif page == "Strategien":
        from pages import strategien
        strategien.show()
    elif page == "Tipp Generator":
        from pages import tipp_generator
        tipp_generator.show()