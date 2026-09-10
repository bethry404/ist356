import streamlit as st

st.title("Saying Hello!!!!")
name = st.text_input("And you are?")
age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

if name:
    st.write(f"Hello, {name}!")

if age:
    st.write(f"You are {age} years old.")

# first time visit the streamlit, hit the refresh button to see the changes.