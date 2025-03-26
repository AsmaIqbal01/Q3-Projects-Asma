import streamlit as st
import re

# Set the page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔏")

# Title and introductory text
st.title("🔐 Password Strength Checker")
st.markdown("""
## Unlock Your Password's Potential! 🔑
Use our handy tool to evaluate your password's strength and receive tailored advice for creating a **Strong Password** 🔒
""")

# Input for password
password = st.text_input("Enter your password:", type="password")

# Initialize feedback and score
feedback = []
score = 0

# Password strength evaluation
if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password should be at least 8 characters long.**")

    # Check for upper and lower case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ **Password should contain both upper and lower case characters.**")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ **Password should contain at least one digit.**")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ **Password should contain at least one special character (e.g., !@#$%^&*).**")

    # Feedback based on score
    if score == 4:
        feedback.append("✅ **Your Password is strong! 🎉**")
    elif score == 3:
        feedback.append("🟡 **Your password is of medium strength. It could be stronger.**")
    else:
        feedback.append("🔴 **Your password is weak. Please make it stronger!**")

# Display feedback
if feedback:
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter your password to get started.")

# Add a footer for additional information
st.markdown("---")
st.markdown("### Tips for Creating a Strong Password:")
st.write("""
- Use a mix of letters, numbers, and special characters.
- Avoid common words and phrases.
- Consider using a passphrase made up of random words.
- Change your passwords regularly and avoid reusing them across different sites.
""")