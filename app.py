import streamlit as st
import cvxpy as cp

st.title("線形最適化問題ソルバー")

# 最適化問題を定義
n = st.slider("変数の数", 2, 10)
x = cp.Variable(n)
obj = cp.Minimize(cp.sum_entries(x))
constraints = [x >= 0]
prob = cp.Problem(obj, constraints)

# 問題を解く
if st.button("解く"):
    result = prob.solve()
    st.success("最適値: {}".format(result))
    st.write("最適解: {}".format(x.value))