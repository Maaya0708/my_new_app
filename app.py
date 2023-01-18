import streamlit as st

st.title("Simple Web App")

name = st.text_input("What's your name?")

if st.button("Greet"):
    result = "Hello, " + name
    st.success(result)


st.title("Simple Calculator")

num1 = st.number_input("Enter a number: ")
num2 = st.number_input("Enter another number: ")

result = ""

if st.button("Add"):
    result = num1 + num2
elif st.button("Subtract"):
    result = num1 - num2
elif st.button("Multiply"):
    result = num1 * num2
elif st.button("Divide"):
    result = num1 / num2

st.write("Result: ", result)