import streamlit as st
from utils.menu import menu
from settings import HOME_PAGE

menu()

st.switch_page(HOME_PAGE)