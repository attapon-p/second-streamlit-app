import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("Enter your name")
c = st.button("Click to show")

if c:
    st.write(f"Hello, {name}!")