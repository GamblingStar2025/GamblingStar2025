
import streamlit as st
from st_supabase_connection import SupabaseConnection

@st.cache_resource
def get_client():
    conn = st.connection("supabase", type=SupabaseConnection)
    return conn.client

def save_strategy(user_email, strategy_name, parameters):
    supabase = get_client()
    data = {
    "email": email,
    "strategy_name": "Heiße Zahlen",
    "parameters": {"anteil": hot},  # statt "einstellungen"
}
    response = supabase.table("strategien").insert(data).execute()
    return response
