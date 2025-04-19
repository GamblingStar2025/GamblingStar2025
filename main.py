# Entry point for Streamlit
import streamlit as st
from utils.session import init_session
from utils.navigation import navigate

init_session()
navigate()