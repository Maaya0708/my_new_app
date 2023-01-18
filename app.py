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


check1=st.checkbox("簡単な計算をして欲しい")
if check1:
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
streamlit run app.py

check2=st.checkbox("翻訳をして欲しい")

if check2:
    st.set_page_config(page_title="翻訳アプリ", page_icon=":guardsman:", layout="wide")
    st.title("翻訳アプリ")

   # 入力されたテキストを取得
    text = st.text_input("翻訳したいテキストを入力してください")

   # 翻訳先の言語を選択
    languages = ["ja", "en", "fr", "es"]
    language = st.selectbox("翻訳先の言語を選択してください", languages)

     # 翻訳ボタンを押した時の処理
    if st.button("翻訳"):
        translator = Translator()
        result = translator.translate(text, dest=language)
        st.success(result.text)
    streamlit run app.py




