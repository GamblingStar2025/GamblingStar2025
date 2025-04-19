import streamlit as st
from utils import check_login
from navigation import show_navigation

check_login()
show_navigation()