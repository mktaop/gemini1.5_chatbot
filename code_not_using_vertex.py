import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader 
import os, fitz, PIL.Image, time


def page_setup():
    st.header("Chat with your PDFs using Gemini 1.5!", anchor=False, divider="blue")
    
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
