
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🧩 Cluster-Strategie", layout="centered")
uploaded_file = st.session_state.get('csv_data', None)
st.title("🧩 Cluster-Strategie")

email = st.session_state.get("user_email", "gast@demo.com")
is_premium = st.session_state.get("is_premium", False)

if not is_premium:
    st.error("🚫 Diese Funktion ist nur für Premium-Nutzer verfügbar.")
    st.info("🔓 [Upgrade auf Premium](https://example.com/upgrade)")
    st.stop()

# CSV wird global aus der Sidebar geladen

@st.cache_data
def lade_zahlen(datei):
    df = pd.read_csv(datei)
    return df.iloc[:, 1:6].values.flatten()

if uploaded_file is not None:
    zahlen = lade_zahlen(uploaded_file)
    hohe = [z for z in zahlen if z > 25]
    niedrige = [z for z in zahlen if z <= 25]
    gerade = [z for z in zahlen if z % 2 == 0]
    ungerade = [z for z in zahlen if z % 2 != 0]

    if len(hohe) >= 2 and len(niedrige) >= 3:
        tipp = random.sample(hohe, 2) + random.sample(niedrige, 3)
        st.success(f"🔢 2 Hoch + 3 Niedrig: {sorted(tipp)}")

    if len(gerade) >= 3 and len(ungerade) >= 2:
        tipp2 = random.sample(gerade, 3) + random.sample(ungerade, 2)
        st.success(f"🔢 3 Gerade + 2 Ungerade: {sorted(tipp2)}")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
