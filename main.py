import streamlit as st
from utils import check_login
from navigation import show_nav

if check_login():
    show_nav()
