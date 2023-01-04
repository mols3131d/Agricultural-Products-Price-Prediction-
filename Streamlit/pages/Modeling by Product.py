import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
# import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pprint
import koreanize_matplotlib
<<<<<<< HEAD:Streamlit/pages/Modeling by Product.py
import altair as alt
=======
>>>>>>> 49b2104d8d2f5feb376c2fa8fee623ce831d4067:Streamlit/Final_Project.py

st.set_page_config(
    page_title="Agriculture",
    page_icon="🚀",
    layout="wide",
)

file = 'AgriMarket.csv'

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data



data = load_data(file)

<<<<<<< HEAD:Streamlit/pages/Modeling by Product.py
=======
st.markdown("## 🚀05~20년도 시장데이터🚀")

st.dataframe(data)


>>>>>>> 49b2104d8d2f5feb376c2fa8fee623ce831d4067:Streamlit/Final_Project.py
data_1 = data.loc[data['Product']=='마늘', ['YMD', 'Price']]
data_1['YM'] = data_1['YMD'].map(lambda x:str(x)[:6])
data_1 = data_1.drop('YMD', axis=1)
data_1 = pd.DataFrame(data_1.groupby('YM')['Price'].mean())

data_2 = data.loc[data['Product']=='감자', ['YMD', 'Price']]
data_2['YM'] = data_2['YMD'].map(lambda x:str(x)[:6])
data_2 = data_2.drop('YMD', axis=1)
data_2 = pd.DataFrame(data_2.groupby('YM')['Price'].mean())

data_3 = data.loc[data['Product']=='고구마', ['YMD', 'Price']]
data_3['YM'] = data_3['YMD'].map(lambda x:str(x)[:6])
data_3 = data_3.drop('YMD', axis=1)
data_3 = pd.DataFrame(data_3.groupby('YM')['Price'].mean())

data_4 = data.loc[data['Product']=='깻잎', ['YMD', 'Price']]
data_4['YM'] = data_4['YMD'].map(lambda x:str(x)[:6])
data_4 = data_4.drop('YMD', axis=1)
data_4 = pd.DataFrame(data_4.groupby('YM')['Price'].mean())
<<<<<<< HEAD:Streamlit/pages/Modeling by Product.py
 

st.markdown("## 품목별 예측 모델링🚀")
=======

st.markdown("## 🚀품목별 데이터🚀")
>>>>>>> 49b2104d8d2f5feb376c2fa8fee623ce831d4067:Streamlit/Final_Project.py

product = ['마늘', '감자', '고구마', '깻잎']
choice = st.selectbox('품목을 선택해주세요.', product)

if choice == product[0]:
    st.markdown("## 🧄마늘")
    st.dataframe(data_1)
    st.markdown("## 가격 추세")
    st.line_chart(data_1)

elif choice == product[1]:
    st.markdown("## 🥔감자")
    st.dataframe(data_2)
    st.markdown("## 가격 추세")
    st.line_chart(data_2)

elif choice == product[2]:
    st.markdown("## 🍠고구마")
    st.dataframe(data_3)
    st.markdown("## 가격 추세")
    st.line_chart(data_3)

elif choice == product[3]:
    st.markdown("## 🍃깻잎")
    st.dataframe(data_4)
    st.markdown("## 가격 추세")
    st.line_chart(data_4)
<<<<<<< HEAD:Streamlit/pages/Modeling by Product.py
    st.get_chart(data)
    



=======
>>>>>>> 49b2104d8d2f5feb376c2fa8fee623ce831d4067:Streamlit/Final_Project.py
