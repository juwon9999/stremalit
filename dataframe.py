import streamlit as st
import pandas as pd

st.title('streamlit dataframe🎨')

dataframe = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second colume' : [10,20,30,40],

})

st.dataframe(dataframe, use_container_width=False)
st.table(dataframe)

st.metric(label="온도", value='10℃', delta="1.2 ℃")
st.metric(label="삼성전자", value="61,000원", delta= "-1,200원")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12,000원")
col2.metric(label="일본JYP(100엔)", value="958.63", delta="-7.44원")
col3.metric(label="유럽연합EUR", value="1,33", delta5.82원="-11.44원")