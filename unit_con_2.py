import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])


def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
    }
    return value * (time_units[to_unit] / time_units[from_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Universal Unit Converter")

# Sidebar Navigation
conversion_type = st.sidebar.selectbox(
    "Select Conversion Type", ["Length", "Weight", "Time", "Temperature"]
)

# Input Fields
value = st.number_input("Enter Value:", min_value=0.0, step=0.1)

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_length(value, from_unit, to_unit)

elif conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_weight(value, from_unit, to_unit)

elif conversion_type == "Time":
    units = ["Seconds", "Minutes", "Hours", "Days"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_time(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_temperature(value, from_unit, to_unit)

# Display Result
st.success(f"Converted Value: {result:.4f} {to_unit}")
