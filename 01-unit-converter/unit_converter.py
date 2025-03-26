import streamlit as st

def convert_units(value, category, unit_from, unit_to):
    # Define conversion factors
    if category == "Length":
        if unit_from == "meter" and unit_to == "Kilometer":
            return value * 0.001
        elif unit_from == "Kilometer" and unit_to == "meter":
            return value * 1000
        elif unit_from == "Kilometer" and unit_to == "miles":
             return value * 0.621371
        elif unit_from == "miles" and unit_to == "Kilometer":
            return value * 1.60934
        elif unit_from == "meter" and unit_to == "miles":
            return value * 0.000621371
        elif unit_from == "miles" and unit_to == "meter":
            return value * 1609.34

    elif category == "Weight":
        if unit_from == "gram" and unit_to =="Kilogram":
            return value * 0.001
        if unit_from == "Kilogram" and unit_to =="gram":
            return value * 1000
    
    elif category == "Time":
        if unit_from == "seconds" and unit_to == "minutes":
            return value / 60
        elif unit_from == "minutes" and unit_to == "seconds":
            return value * 60
        elif unit_from == "minutes" and unit_to == "hours":
            return value / 60
        elif unit_from == "hours" and unit_to == "minutes":
            return value * 60
        elif unit_from == "hours" and unit_to == "days":
            return value / 24
        elif unit_from  == "days" and unit_to == "hours":
            return value *24

    return None             

# Streamlit UI
st.title("🌍Unit Converter App")
st.markdown("### Converts Length, Weight and Time instantly")
st.write("Welcome! Select a Category, Enter value and get converted values in real time.")
category = st.selectbox("Choose a Catgory",["Length","Weight","Time"])


value = st.number_input("Enter the value to convert:", min_value=1.0, step=1.0)

if category == "Length":
    unit_from = st.selectbox("📏Convert from:", ["meter", "kilometer","miles"])
    unit_to = st.selectbox("📏Convert to:", ["meter", "kilometer", "miles"])
elif category == "Weight":
    unit_from =st.selectbox("⚖Convert from:",["gram","Kilogram"])
    unit_to =st.selectbox("⚖Convert to:",["gram","Kilogram"])
else: # Time Category
    unit_from =st.selectbox("⏰Convert from:",["seconds","minutes","hours","days"])
    unit_to = st.selectbox("⏰Convert to:",["seconds","minutes","hours","days"])
if st.button("Convert"):
    result = convert_units(value, category,unit_from, unit_to)
    if result is not None:
        st.write(f"Converted value: {result:.4f} {unit_to}")
    else:
        st.write("Conversion 🎞not supported for the selected units.")