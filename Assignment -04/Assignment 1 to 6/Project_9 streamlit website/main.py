import streamlit as st
from deep_translator import GoogleTranslator

# Set the title of the app
st.title("Simple Translator App")

# Initialize session state for text_to_translate if it doesn't exist
if 'text_to_translate' not in st.session_state:
    st.session_state.text_to_translate = ""

# Create a text input for the user to enter text
text_to_translate = st.text_area("Enter text to translate:", value=st.session_state.text_to_translate)

# Create a dropdown for selecting the target language
languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional)': 'zh-TW',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Arabic': 'ar',
    'Urdu': 'ur',
    'Hindi': 'hi',
    'Persian': 'fa',
    'Sindhi': 'sd',      # Added Sindhi
    'Pashto': 'ps',      # Added Pashto
    'Gujarati': 'gu',
    'Turkish': 'tr'
}

target_language = st.selectbox("Select target language:", list(languages.keys()))

# Slider for font size
font_size = st.slider("Select font size for translated text:", 10, 50, 20)

# Button to perform translation
if st.button("Translate"):
    if text_to_translate:
        # Translate the text
        try:
            translated = GoogleTranslator(source='auto', target=languages[target_language]).translate(text_to_translate)
            st.markdown(f"<h2 style='font-size: {font_size}px;'>Translated text:</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: {font_size}px;'>{translated}</p>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.error("Please enter text to translate.")

# Function to clear the text area
def clear_text():
    st.session_state.text_to_translate = ""  # Clear the session state value
    st.rerun()  # Rerun the app to refresh the input field

# Button to clear input
if st.button("Clear"):
    clear_text()

# Add some information about the app
st.markdown("""
This is a simple translator app built with Streamlit and Deep Translator API.
You can enter text in the text area above and select a target language to see the translation.
Adjust the font size of the translated text using the slider.
""")