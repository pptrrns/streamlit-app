import streamlit as st
from utils.ui import *

def menu():
    """
    Configures and displays the sidebar menu for the Streamlit application.
    
    Parameters
    ----------
    None
    """
    if "set_page_config" not in st.session_state:
        st.session_state.set_page_config = st.set_page_config(
            page_title=PAGE_TITLE,
            page_icon=PAGE_ICON,
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "Get Help": HELP_URL,
                "Report a bug": BUG_REPORT_URL,
                "About": PAGE_TITLE,
            },
        )

    st.sidebar.image("assets/aio.png",
                     use_column_width=True)
    
    st.sidebar.markdown("---")
    
    st.sidebar.page_link("pages/0_home.py", label="Lorem Ipsum")

    hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            header {visibility: visible;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)