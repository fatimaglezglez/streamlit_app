import streamlit as st

st.set_page_config(page_title="Fatima's App",
                   page_icon=":pink_heart:",
                   layout="centered")

# Display a header
st.markdown("# Welcome to my simple app :)")

# Input for the user's name
name = st.text_input('What is your name?', '')

# Dropdown for selecting favorite color
color = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Green', 'Red', 'Yellow', 'Orange', 'Purple', 'Pink')
)

# Change the background color based on the user's favorite color
color_hex = {
    'Blue': '#0000FF',
    'Green': '#008000',
    'Red': '#FF0000',
    'Yellow': '#FFFF00',
    'Orange': '#FFA500',
    'Purple': '#800080',
    'Pink': '#FFC0CB',
}.get(color, '#FFFFFF') # Default to white if the color is somehow not in the list

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color_hex};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display the personalized greeting
if name:
    st.write(f'Hello, {name}! You have chosen {color} as your favorite color.')

