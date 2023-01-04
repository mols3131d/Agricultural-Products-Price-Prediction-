import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pprint
import koreanize_matplotlib
import altair as alt
from PIL import Image


st.set_page_config(
    page_title="Agriculture",
    page_icon="🌾",
    layout="wide",
)

file = 'AgriMarket.csv'

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

df = load_data(file)
df.columns = ["YMD","YM","MD","Product","Price","Cereals","Food Price Index","item_CPI","item_PPI","콜금리(연%)","환율(원/US$"]

st.header(" 🌾 Agricultural Products Price Prediction")

st.markdown("""       """)
# st.dataframe(df)

st.markdown("## ✔ 품목별 EDA")
st.markdown("")
tab1, tab2, tab3, tab4 = st.tabs(["🧄 마늘","🥔 감자", "🍠고구마", "🍃 깻잎" ])

with tab1:
    df_g = df[df["Product"] == "마늘"]
    df_g["M"] = df_g['MD'].map(lambda x:str(x)[:-2])
    df_g["Y"] = df_g['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_g.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_g.groupby('M')['Price'].sum())
          
    plt.figure(figsize=(20, 7))
    st.markdown("")
    st.markdown("💡 9 ~ 10월에 심어서 5 ~ 6월에 수확")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)

with tab2:
    df_p = df[df["Product"] == "감자"]
    df_p["M"] = df_p['MD'].map(lambda x:str(x)[:-2])
    df_p["Y"] = df_p['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_p.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_p.groupby('M')['Price'].sum())


    st.markdown("- 봄감자:  2 ~ 4월 사이에 심어서 ")
    st.markdown("- 가을감자: 8월말까지 심어서 ")
    st.markdown("** 지역별로 90 ~ 100 일 정도재배 후 수확 ** ")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)

with tab3:
    df_sp = df[df["Product"] == "고구마"]
    df_sp["M"] = df_sp['MD'].map(lambda x:str(x)[:-2])
    df_sp["Y"] = df_sp['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_sp.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_sp.groupby('M')['Price'].sum())


    plt.figure(figsize=(20, 7))
    sns.lineplot(data=df_sp, x="M", y=df_sp["Price"])
    st.markdown("가을~겨울 온도가 낮아질수록 수요증가 (군고구마) + 여름 이상기온 많을수록 공급감소 ")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)

with tab4:
    df_k = df[df["Product"] == "깻잎"]
    df_k["M"] = df_k['MD'].map(lambda x:str(x)[:-2])
    df_k["Y"] = df_k['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_k.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_k.groupby('M')['Price'].sum())
  
    st.markdown("💡 4~5월에 심어서 봄에는 4-50일, 여름 파종은 40일 후 수확")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)




st.markdown("")
st.markdown("---")
st.markdown("")