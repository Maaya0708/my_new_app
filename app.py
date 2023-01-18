import streamlit as st

st.title("計算機")
st.write("ここでは簡単な計算をします")

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


Stop generating
