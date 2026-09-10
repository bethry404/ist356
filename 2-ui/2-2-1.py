import streamlit as st

st.title("Rectangle Area and Perimeter Calculator")

length = st.number_input("Enter length: ")
width = st.number_input("Enter width: ")


col1, col2, col3 = st.columns([0.2, 0.15, 1])
with col1:
    btn_clicked = st.button("Calculate")
with col2:
    btn_clear = st.button("Clear")


if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.success(f"Area: {area}, Perimeter: {perimeter}")

if btn_clear:
    length = 0
    width = 0
    st.success(f"Length and width cleared. Please enter new values.")


