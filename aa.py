import streamlit as st

st.title('DAESINSA 🎈')
st.title("(❁´◡`❁)")

st.header('학교소개')
st.subheader('교육활동')
st.caption('학급마당')

sample_code = '''
    def function():
        print('hello, world')
'''

st.code(sample_code, language='python')

st.text('텍스트')

st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다.')
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")