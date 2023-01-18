import streamlit as st

st.title("計算機")
st.write("ここでは")

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
アプリを実行します。streamlit run [ファイル名].py

ブラウザでアプリにアクセスします。http://localhost:8501/

"Simple Calculator"というタイトルが表示され、2つの数字を入力するための入力ボックスが表示されます。加算、減算、乗算、除算のいずれかのボタンをクリックして、結果を計算します。

これは簡


Stop generating
