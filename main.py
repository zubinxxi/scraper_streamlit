import streamlit as st 

from shortener import shortener
from scraper import scraper

st.set_page_config(
    page_icon="assets/favicon.ico",
    page_title="SCRAPER | Streamlit"
)

tab1, tab2 = st.tabs(
    [
        "URL Shortener", "Wikipedia Web Scraper"
    ]
)

with tab1:
    shortener()

with tab2:
    scraper()