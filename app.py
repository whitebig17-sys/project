import streamlit as st

st.title("用streamlit架站")
st.header("網頁標題")

with st.sidebar:
    st.header("選單標題")
    st.write("選單內容")
    st.button("按鈕A")
    st.button("按鈕K")
  

#網頁 footer bottom 聯絡資訊
st.bottom.header("關於我")
st.bottom.text("聯絡資訊: email: whitebig17@gmail.com")