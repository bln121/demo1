import streamlit as st
import sqlite3
import bcrypt
import urllib.request


def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "Narayana":
            st.write("Login sucessful")
login_page() 
 
    

