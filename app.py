import streamlit as st
import sqlite3
import bcrypt

# Connect to the SQLite database

def create_database():    
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='users'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE users
                     (username text, password text)''')
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
    # Hash the password
    #hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    conn = sqlite3.connect('users1.db')
    c = conn.cursor()
    # Insert user data into the database
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

    st.success("Signup successful! Please proceed to login.")
    view_customers()

def check_credentials(username, password):
    # Retrieve the user data from the database
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        # Verify the password
        if bcrypt.checkpw(password.encode("utf-8"), user[2]):
            st.success("Login successful!")
            # Set a session token or identifier
            # You can use Streamlit's SessionState module or another method of your choice
            # to store the session state and authenticate subsequent requests
        else:
            st.error("Incorrect password. Please try again.")
    else:
        st.error("User not found. Please sign up first.")

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
    signup_page()
    #login_page()
else:
    st.title("Dashboard")
    st.write("This is the authenticated area of the app.")
    # Add your main application code here

# Close the database connection when the Streamlit app is stopped
#conn.close()

