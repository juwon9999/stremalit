import streamlit as st
import pandas as pd


st.header('BMW 모델 라인업')
name = option = st.selectbox(
    '필터',
    ('차량 전체보기','플러그인 하이브리드', '순수 전기', 'BMW I','BMW M','선택사항 없음'),
    index=5
)

if name == '플러그인 하이브리드':
    col1, col2, col3 = st.columns(3)
    with col1:
        st.sudheader("BMW 뉴 XM")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/m-series/xm/2022/Highlights/bmw-x-series-xm-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1662477770743.jpg")
    with col2:
        st.subheader("BMW 뉴 3")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/3-series/sedan/2022/highlights/bmw-3-series-sedan-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1651158408008.jpg")
    with col3:
        st.subheader("BMW 뉴 X5")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/x-series/x5/2023/highlights/bmw-x-series-x5-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1673960417242.jpg")

elif name == '순수 전기':
    col11, col22, col33 = st.columns(3)
    with col11:
        st.subheader("BMW 뉴 XM")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/m-series/xm/2022/Highlights/bmw-x-series-xm-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1662477770743.jpg")
    with col22:
        st.subheader("BMW 뉴 3")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/3-series/sedan/2022/highlights/bmw-3-series-sedan-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1651158408008.jpg")
    with col33:
        st.subheader("BMW 뉴 X5")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/x-series/x5/2023/highlights/bmw-x-series-x5-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1673960417242.jpg")
elif name == 'BMW M':
    col11, col22, col33 = st.columns(3)
    with col11:
        st.subheader("BMW 뉴 XM")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/m-series/xm/2022/Highlights/bmw-x-series-xm-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1662477770743.jpg")
    with col22:
        st.subheader("BMW 뉴 3")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/3-series/sedan/2022/highlights/bmw-3-series-sedan-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1651158408008.jpg")
    with col33:
        st.subheader("BMW 뉴 X5")
        st.image(
            "https://www.bmw.co.kr/content/dam/bmw/common/all-models/x-series/x5/2023/highlights/bmw-x-series-x5-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1673960417242.jpg")

elif name == 'BMW I':
    st.caption("검색차량 없음")
    st.write("필터 기준에 맞는 차량이 없습니다. 필터를 재설정하여 검색해 보세요.")
    


check=st.checkbox('더 많은 필터보기')

if check:
    st.caption("필터")
    st.subheader("바디타입")
    col001, col002, col003 = st.columns(3)
    with col001:
        t = st.checkbox('🚗투어링')
    with col002:
        s = st.checkbox('🚗세단')
    with col003:
        r = st.checkbox('🏎로드스터')
    st.subheader("엔진 종류")
    col004, col005, col006 = st.columns(3)
    with col004:
        st.checkbox('가솔린')
    with col005:
        st.checkbox('플러그인 하이브리드')
    with col006:
        st.checkbox('디젤')

    col007, col008 = st.columns(2)
    with col007:
        number = st.number_input('가격을 입력하세요')
        st.write('The current number is ', number)

    with col008:
        number2 = st.number_input('가격을 입력하세요')
        st.write('The current number is ', number2)





