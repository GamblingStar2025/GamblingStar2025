
from supabase import create_client
import streamlit as st

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

def save_strategy(email, strategy_name, parameters):
    data = {
        "email": email,
        "strategy_name": strategy_name,
        "parameters": parameters
    }
    response = supabase.table("Strategien").insert(data).execute()
    return response
