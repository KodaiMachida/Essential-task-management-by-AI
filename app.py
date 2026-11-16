import streamlit as st

st.title("Essential Task Management by AI")

st.header("① 将来目標の設定")

big_goal = st.text_area("大目標（長期的な目標）")
medium_goal = st.text_area("中目標（数年以内の目標）")
small_goal = st.text_area("小目標（直近の目標）")

st.header("② 現在のタスク")

task = st.text_area("現在取り組んでいるタスク")

if st.button("AIでタスクを評価"):
    if all([big_goal, medium_goal, small_goal, task]):
        st.success("入力が完了しました！")
        st.write("大目標：", big_goal)
        st.write("中目標：", medium_goal)
        st.write("小目標：", small_goal)
        st.write("タスク：", task)
    else:
        st.warning("すべての項目を入力してください。")