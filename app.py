import streamlit as st

st.title("Simple Web App")

name = st.text_input("What's your name?")

if st.button("Greet"):
    result = "Hello, " + name
    st.success(result)
