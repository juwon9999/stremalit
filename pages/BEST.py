import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)

with col1:
   st.header("BMW I7")
   st.image("https://www.bmw.co.kr/content/dam/bmw/marketKR/bmw_co_kr/all-models/i-series/i7-desktop.png/jcr:content/renditions/cq5dam.resized.img.1680.large.time1678782047312.png")
   button1 = st.button("BMW I7 설명보기")
   if button1:
       st.write("지능형 사륜구동 시스템 BMW xDrive를 장착한 BMW i7 M70 xDrive는 두 개의 강력한 BMW M eDrive 전기 모터로 구동되며 합산 최고 출력 660마력*의 퍼포먼스를  선보입니다. 이산화탄소 배출 없는 순수 전기 모델로 1회 충전 시 최대 560km*까지 주행 가능합니다. BMW M만의 다양한  최신 기술과 고급스러운 디자인 요소가 더해져 최상의 주행 경험을 제공합니다.")
   button2 = st.button("BMW I7 영상보기")
   if button2:
       st.video('https://www.youtube.com/watch?v=vFH6K-1Sb0U', 'rb')
with col2:
   st.header("BMW I7 M70")
   st.image("https://www.bmw.co.kr/content/dam/bmw/common/all-models/m-series/m760e-xdrive/2023/highlights/bmw-7-series-i7-m70-sp-desktop_clean.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1681472202471.jpg")
   button3 = st.button("BMW I7 M70 설명보기")
   if button3:
       st.write("BMW i7은 럭셔리 순수전기 드라이빙의 새로운 기준을 제시하는 BMW 미래 플래그십 모델로, BMW 7시리즈의 순수전기 모델입니다. 약 438km* 주행 가능 거리를 자랑하는 전기 배터리와 멀티센서 엔터테인먼트의 결합은 최상의 주행 경험을 제공하며, 크리스탈 헤드라이트 및 BMW ‘아이코닉 글로우‘ 키드니 그릴은 BMW 7시리즈의 존재감을 드러냅니다. 개별 My Modes 기능으로 고급스러운 라운지 분위기 연출이 가능하며, 31.3인치의 시어터 스크린으로 마치 영화관과 같은 경험을 즐길 수 있습니다.")
   button4 = st.button("BMW I7 M70 영상보기")
   if button4:
       st.video('https://www.youtube.com/watch?v=WpNixyXQV1U', 'rb')
with col3:
   st.header("BMW IX M60")
   st.image("https://www.bmw.co.kr/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-sp-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1642436756384.jpg")
   button5 = st.button("BMW IX M60 설명보기")
   if button5:
       st.write("BMW iX M60 은 BMW i의 기술과 BMW M의 혁신적인 파워를 결합한 모델입니다. 2개의 BMW M eDrive 모터로 구동되는 순수전기 구동 차량인 BMW iX M60은 전기 4륜 구동으로 540마력의 퍼포먼스를 뿜어냅니다. 새로운 기술 덕분에 이산화탄소 배출이 전혀 없는 짜릿한 주행 쾌감과 최대 421km의 1회 충전 주행 가능 거리를 제공합니다. 이러한 최신 기술에 고급스러운 분위기의 인테리어가 더해져 시선을 사로잡습니다.")
   button6 = st.button("BMW IX M60 영상보기")
   if button6:
        st.video('https://www.youtube.com/watch?v=fHo4igYQEy4', 'rb')
