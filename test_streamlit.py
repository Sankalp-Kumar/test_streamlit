import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Text input
user_input = st.text_input("Enter your name:")

# Dropdown selection
options = st.selectbox("What's your favorite programming language?", 
                       ['Python', 'JavaScript', 'Java', 'C++', 'Other'])

# Displaying the input
if user_input:
    st.write(f"Hello, {user_input}!")

# Displaying selected option
if options:
    st.write(f"Your favorite programming language is {options}.")

# Adding a slider
age = st.slider("Select your age:", 0, 100, 25)

# Displaying slider value
st.write(f"You are {age} years old.")

# Adding a button
if st.button('Click me'):
    st.write("Button clicked!")

# Displaying some data
import pandas as pd
import numpy as np

# Create a simple DataFrame
data = pd.DataFrame({
    'Column A': np.random.randn(10),
    'Column B': np.random.randn(10)
})

# Display the DataFrame
st.write("Here is a random DataFrame:")
st.write(data)

# Line chart
st.line_chart(data)
