import pandas as pd
import streamlit as st
from databricks import sql
from databricks.sdk.core import Config
from utils.db_connection import DB_Query
from utils.db_query import *
from utils.menu import menu
from settings import *
from utils.ui import *

#----- ----- -----

menu()

#----- ----- -----

db_kids = DB_Query.get_query(GET_KIDS, schema = "causal_ai_prod", table = "active_clients_", country = "mx")

#----- ----- -----

st.sidebar.info(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tristique gravida hendrerit. Nam porttitor enim nec ipsum sodales, sed vehicula nibh porttitor.
    """
)

#----- ----- -----

col_logo, col_content = st.columns([1, 8])

with col_logo:
    st.image(LOGO_PATH)
    
with col_content:
    st.markdown(f"""
    <div style="padding: 20px; border-radius: 10px; margin-bottom: 20px; background-color: #f8f9fa; border-left: 5px solid {BRAND_COLOR};">
        <h2 style="color: {BRAND_COLOR}; margin-top: 0;">{INITIATIVE}</h2>
        <p style="margin-bottom: 10px;">{FEATURE}</p>
    </div>
    """, unsafe_allow_html=True)

#----- ----- -----

st.markdown("<br>", unsafe_allow_html=True)

#----- ----- -----

st.markdown("<h3>{FEATURE}</h3>", unsafe_allow_html=True)