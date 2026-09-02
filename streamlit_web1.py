import streamlit as st

# (A) CONTENTS
st.title("研究專題名稱")
st.divider()

# 若 images/logo.png 不存在，執行時會跳出警告，請確保檔案路徑正確
# st.logo("images/logo.png", size="large")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        "<p style='font-size:24px; font-weight:bold;'>預防肺癌與護肺要點</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='font-size:14px;'>5大肺癌預防與護肺要點：<br>"
        "戒菸與遠離菸害：吸菸是導致肺癌最大的危險因子。</p>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        "<p style='font-size:24px; font-weight:bold;'>治療肺癌與護肺要點</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='font-size:14px;'>"
        "減少廚房油煙：高溫煎、炒容易產生有害油煙。</p>",
        unsafe_allow_html=True
    )

st.divider()
c1 = st.container()

with c1:
    st.markdown("""
    **5大肺癌預防與護肺要點**
    * **戒菸與遠離菸害**：吸菸是導致肺癌最大的危險因子，吸菸者及經常接觸二手菸、三手菸的民眾風險大增，應盡早戒菸並拒絕菸害。
    * **減少廚房油煙**：高溫煎、炒容易產生有害油煙。烹調時建議多用蒸、煮或低溫水炒，務必開啟抽油煙機，並保持廚房通風。
    * **防範環境與職業暴露**：避免長期接觸重金屬、石棉、柴油廢氣或有害化學物質，工作時應確實穿戴防護裝備。
    """)

# 請確保本機/伺服器上有 images/img01.jpg 檔案
st.image("images/img01.jpg", caption="肺癌預防與護肺要點")

tab1, tab2, tab3 = st.tabs(["預防肺癌與護肺要點", "治療肺癌與護肺要點", "關於肺癌"])

with tab1:
    st.header("預防肺癌與護肺要點")
    st.image("images/img01.jpg", caption="肺癌預防與護肺要點")

with tab2:
    st.header("治療肺癌與護肺要點")
    st.image("images/img01.png", caption="肺癌治療與護肺要點")

with tab3:
    st.video("https://www.youtube.com/watch?v=Bz-UCPP8fMo&t=333s", start_time=0)


# (B) LEFT
with st.sidebar:
    with st.container():
        st.header("選單標題1")
        st.write("選單內容1")
        st.button("按鈕A1")
        st.button("按鈕K1")


# (C) FOOTER
st.divider()

st.header("關於我")
st.text("聯絡資訊: email:")