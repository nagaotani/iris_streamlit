from msilib.schema import Condition
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 基礎')
st.write('Hello World!')

df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [10, 20, 30, 40]
})

st.dataframe(df)

st.dataframe(df.style.highlight_max(axis=0), width=100,
                height=150)

st.table(df)

df = pd.DataFrame(
    np.random.rand(10, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [42.3142, 140.9742],
    columns=['lat', 'lon']
)

st.map(df)

from PIL import Image

img = Image.open('iris.jpg')
st.image(img, caption='Iris', use_column_width=True)

if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img, caption='Iris', use_column_width=True)

option = st.selectbox(
    '好きな数字を入力してください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です。'

#text = st.text_input('あなたの好きなスポーツを教えてください。')

#'あなたの好きなスポーツ：', text

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'コンディション：', condition

text = st.sidebar.text_input('あなたの好きなスポーツを教えてください。')

'あなたの好きなスポーツ：', text

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

expander1 = st.expander('質問1')
expander1.write('質問1の回答')
expander2 = st.expander('質問2')
expander2.write('質問2の回答')
expander3 = st.expander('質問3')
expander3.write('質問3の回答')

import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'
