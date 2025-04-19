import streamlit as st

def show_navigation():
    pages = {
        "📊 Dashboard": "pages/dashboard.py",
        "📁 CSV Upload": "pages/upload_csv.py",
        "♟️ Strategien": "pages/strategien.py",
        "🔮 Tipp Generator": "pages/tipp_generator.py",
        "💾 Meine Strategien": "pages/meine_strategien.py",
        "🔐 Logout": "pages/logout.py"
    }
    choice = st.sidebar.radio("Navigation", list(pages.keys()))
    st.switch_page(pages[choice])