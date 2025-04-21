import streamlit as st
import hashlib
from cryptography.fernet import Fernet

#------setup---------
# Generate a key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Session state initialization
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # {"encrypted_text": {"encrypted_text": ..., "passkey": ...}}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

#----------utility Functions------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    entry = st.session_state.stored_data.get(encrypted_text)

    if entry and entry['passkey'] == hashed:
        st.session_state.failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    else:
        st.session_state.failed_attempts += 1
        return None

#-----UI------
st.title("🔒 Secure Data Encryption System")
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home page
if choice == "Home":
    st.subheader("🏠 WELCOME")
    st.write("This app allows you to securely store and retrieve sensitive data using encryption and passkey protection.")

# Store Data Page
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter the data you want to encrypt:")
    passkey = st.text_input("Set a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data)
            hashed = hash_passkey(passkey)
            st.session_state.stored_data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed
            }
            st.success("✅ Data encrypted and stored!")
            st.code(encrypted, language='text')
        else:
            st.warning("⚠️ Please enter both data and passkey.")

# Retrieve Data page
elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3 and not st.session_state.authenticated:
        st.warning("🚫 Too many failed attempts. Redirecting to Login.")
        st.experimental_rerun()

    st.subheader("🔍 Retrieve your Data")
    encrypted_text = st.text_area("Enter encrypted data:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success("✅ Data decrypted successfully!")
                st.code(result, language="text")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts. Please log in again.")
                    st.session_state.authenticated = False
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Please provide both encrypted data and passkey.")

# Login Page
elif choice == "Login":
    st.subheader("🔐 Login for reauthorization")
    login_pass = st.text_input("Enter Master Password:", type="password")
    if st.button("Login"):
        if login_pass == "admin123":
            st.success("✅ Logged in successfully!")
            st.session_state.failed_attempts = 0
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect Master password!")
