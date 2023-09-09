import streamlit as st
import pandas as pd

st.title('BMW')
st.subheader('BMW VISION NEUE KLASSE')
st.caption('BMW 비전 노이어 클라쎄. 새로운 시대의 모빌리티')
st.image("https://bmw.scene7.com/is/image/BMW/BMW-Finance-Promotion-v2?wid=1504&hei=853")
st.header('지금 바로 BMW를 경험해보세요.')
col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("시승 신청")
   st.image("https://bmw.scene7.com/is/image/BMW/NxW_Home_ICON_TESTDRIVE?wid=1504&hei=542")
   button1 = st.button("시승 신청 바로가기")
with col2:
   st.subheader("내 차량 만들기")
   st.image("https://bmw.scene7.com/is/image/BMW/NxW_Home_ICON_USED_CAR?wid=1504&hei=542")
   button2 = st.button("내 차량 만들기 바로가기")
with col3:
   st.subheader("BMW 샵 온라인")
   st.image("https://bmw.scene7.com/is/image/BMW/NxW_Home_ICON_CON?wid=1504&hei=542")
   button3 = st.button("BMW 샵 온라인 바로가기")
st.caption('개인정보 처리방침')
