import streamlit as st
import sqlite3
import bcrypt
import urllib.request

# Connect to the SQLite database

url = 'https://raw.githubusercontent.com/bln121/demo1/main/users1.db'
urllib.request.urlretrieve(url, 'users1.db')


def create_database():    
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='users'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE users
                     (username text primary key, password text)''')
        conn.commit()
    conn.close()

def view_customers():
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    st.write(users)
   # return customers


def save_credentials(username, password):
   
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()
    # Insert user data into the database
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

    st.success("Signup successful! Please proceed to login.")
    view_customers()

def check_credentials(uname, password):
    # Retrieve the user data from the database
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()

    c.execute('SELECT password FROM users WHERE username = ?', (uname,))
    pas = c.fetchone()
    st.write(pas)

    if pas:
        db_pass=pas[0]
        if db_pass==password:
            st.success("Login successful")
        

def signup_page():
    st.header("Sign Up")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        save_credentials(username, password)

def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        check_credentials(username, password)

session_state = st.session_state

if not session_state.get("logged_in"):
    st.title("Welcome to My App")
    create_database()
    choice = st.radio("Choose an action:", ("Signup", "Login"))

    if choice == "Signup":
        signup_page()
    elif choice == "Login":
        login_page()
    #signup_page()
    #login_page()
else:
    st.title("Dashboard")
    st.write("This is the authenticated area of the app.")
    # Add your main application code here

# Close the database connection when the Streamlit app is stopped
#conn.close()

