import streamlit as st

st.title("あなたのことを教えて")

name = st.text_input("What's your name?")

if st.button("Greet"):
    result = "Hello, " + name
    st.success(result)

st.radio("性別は？", ("男", "女", "その他"))
st.radio("所属は？", ("学生", "社会人", "その他"))

st.write("何をしにこのサイトに来ましたか？")
st.checkbox("簡単な計算をして欲しい")
st.checkbox("翻訳をして欲しい")

st.title("簡単な計算")
st.write("ここでは簡単な計算をします")

num1 = st.number_input("Enter a number: ")
num2 = st.number_input("Enter another number: ")

result = ""
    
if st.button("Add"):
    result = num1+ num2
elif st.button("Subtract"):
    result = num1 - num2
elif st.button("Multiply"):
    result = num1 * num2
elif st.button("Divide"):
    result = num1 / num2

st.write("Result: ", result)
    
    
