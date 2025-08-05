import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./data/mydata.csv')

# gloval variable
url='https://www.youtube.com/watch?v=XyEOEBsa8I4'

#dictionary
ulrs={
    '윤리':['1','2'],
    '코딩':['3','4']
}

st.title('This si my first  webapp!!')
col1, col2=st.columns((4,1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(url)
    
    with st.expander('SubContent2...'):
        st.subheader('Image Content...')
        st.image('./images/catdog.jpeg')
    
    with st.expander('SubContent3...'):
        st.subheader('html Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html','r',encoding='utf-8') as f:
            html1=f.read()
            f.close()
        htmlviewer.html(html1, height=800)

    with st.expander('SubContent4...'):
        st.subheader('data app Content...')
        st.table(df)
        st.write(df.describe())
        fig, ax=plt.subplots(figsize=(20,10))
        df.plot(ax=ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png')
        st.plotly_chart(df)

with col2:
    with st.expander('Tips...'):
        st.info('Tips...')