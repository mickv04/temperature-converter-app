
# -----------------------------------
# TEMPERATURE CONVERTER WEB APP
# Built using Python and Streamlit
# -----------------------------------

# Step 1: Import the Streamlit library
import streamlit as st

# Step 2: Set up the webpage
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

# Step 3: Display the title and instructions
st.title("🌡️ Temperature Converter")

st.write("Welcome to the Temperature Converter!")

st.write(
    "Enter a temperature, select a conversion type, "
    "and click the button to see your result."
)

# Step 4: Allow the user to enter a temperature
temperature = st.number_input(
    "Enter a temperature:",
    value=0.0,
    step=1.0
)

# Step 5: Let the user choose a conversion type
conversion_type = st.selectbox(
    "Select conversion type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
)

# Step 6: Create a button to calculate the result
if st.button("Convert Temperature"):

    # Step 7: Check which conversion the user selected
    if conversion_type == "Celsius to Fahrenheit":

        # Convert Celsius to Fahrenheit
        converted_temp = (temperature * 9/5) + 32

        # Display the result
        st.success("Conversion completed!")

        st.metric(
            label="Converted Temperature",
            value=f"{converted_temp:.2f} °F"
        )

        # Show the formula used
        st.subheader("Conversion Formula")

        st.write("°F = (°C × 9/5) + 32")

        st.write(
            f"({temperature} × 9/5) + 32 = "
            f"{converted_temp:.2f} °F"
        )

    else:

        # Convert Fahrenheit to Celsius
        converted_temp = (temperature - 32) * 5/9

        # Display the result
        st.success("Conversion completed!")

        st.metric(
            label="Converted Temperature",
            value=f"{converted_temp:.2f} °C"
        )

        # Show the formula used
        st.subheader("Conversion Formula")

        st.write("°C = (°F - 32) × 5/9")

        st.write(
            f"({temperature} - 32) × 5/9 = "
            f"{converted_temp:.2f} °C"
        )

# Step 8: Add a footer
st.divider()

st.caption("Temperature Converter | Built with Python and Streamlit")
