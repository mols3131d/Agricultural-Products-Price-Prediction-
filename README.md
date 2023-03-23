# Agricultural-Products-Price-Prediction-


# Index

# Summary

- 농산품 시장은 전통적으로 변동성이 큰 시장으로 알려져 있었는데, 최근 여러 요인으로 인해 변동성이 더욱 커졌으며, 이에 따라 생산자와 소비자에게 부정적인 영향을 주고 있다.
    
    본 프로젝트는 농산품 시장 관련 데이터를 탐색해보고, 가격 예측을 진행하여 농산물 시장의 불안정한 경제상황에 대비하고 대응하는 것에 기여하는 것을 기대하여 진행하였다.
    
- 본 프로젝트는 아래의 절차로 진행되었다.
    1. 데이터 선정 및 수집
    2. EDA
    3. 농산품 가격 예측
        - `ARIMA` `SARIMA` `SARIMAX` `Prophet`
- 농산품 가격과 주산지 기상 데이터 EDA에서 2011년 전후로 큰 차이를 확인하였다. 추가적으로 조사한 결과, 이상기후에의한 생산량 감소가 있었음을 알 수 있었다.
    
    `SARIMAX` 모델로 품목의 물가지수와 국제가격지수 그리고 환율와 콜금리를 변수로 설정하였을 때,  `MAE`값이 `1269.593`로 가장 높은 예측성능을 보였다.
    

# Output

- [Google Slide](https://docs.google.com/presentation/d/1MiEM-Mo72EeKbuoDuNkexDcOcm00g1u__conYAksmgw/present)
    
    [https://docs.google.com/presentation/d/1MiEM-Mo72EeKbuoDuNkexDcOcm00g1u__conYAksmgw/present](https://docs.google.com/presentation/d/1MiEM-Mo72EeKbuoDuNkexDcOcm00g1u__conYAksmgw/present)
    
- [Youtube](https://youtu.be/_8r2QF7Jzj8)
    
    [https://youtu.be/_8r2QF7Jzj8](https://youtu.be/_8r2QF7Jzj8)
    
- [GitHub](https://github.com/Sankamita3131/Agricultural-Products-Price-Prediction-)
- [Streamlit](https://y0ungbinlee-test-1-main-gfhk1e.streamlit.app/)

# 개요

## 주제

- 농산품 시장과 관련된 데이터를 수집, 분석하여 농산품 시장의 특징을 알아보고 경제 데이터와 기상정보를 활용하여 농산품 가격을 예측해보는 프로젝트

## 배경

- 식량안보 문제
- 곡물 자급률
- 수입 의존도
- 외교 분쟁
- 경기 침체
- 기후 변화

## 선행연구

- **정민제 & 최영찬. (2020). 인공신경망 가격 예측 모델. 농식품신유통연구원.**
    
    위의 연구에서는 **농산물 가격은 높은 변동성**을 지고 있으므로, **소비자와 생산자의 불안정성을 유발**한다고 보았다. 정교한 가격예측모델 개발을 위해서는 충분한 양의 산지유통 조직의 데이터가 필요함과 인공신경망과 같은 기계학습 기반의 방법이 적절함을 시사하였다.
    
- **최병옥 & 최익창. (2007). 시계열 분석방법을 이용한 과채류 월별가격 예측. KREI 한국농촌경제연구원.**
    
    위의 연구에서는 생산자가 공급량과 가격예측에 어려움을 겪고 있어 가격 예측이 필요하다고 보았다.
    그리고  **ARMA 모형**이 오이와 같은 생산대체 관계가 적은 품목에서는 좋은 예측결과를 보였다.
    

## 기대효과

- 불안정한 경기 속 농산품 가격 예측을 통한 대비 또는 대비 방안 마련

# 분석

## 데이터 선정 및 수집

- **농산품 시장 관련 데이터**
    - aT 농수축산물 일자별 도소매 가격
    - FAO Food Price Index
    - FAO Cereal Price Index
    - 품목별 생산자물가지수
    - 품목별 소비자물가지수
- **거시 경제 지표 관련 데이터**
    - 환율(원/US$)
    - 콜금리(연%)
- **농업 기상 정보 데이터**
    - 기상청_작물별 농업주산지 상세날씨 조회서비스

## EDA

- EDA 결과
    - 가격의 변화와 주산지의 기후데이터를 보았을 때, 2011년 전후로 큰 차이를 확인하였다.
    - 이를 바탕으로 추가적으로 조사한 결과, 이상기후에의한 생산량 감소로 인한 가격증가가 있었음을 알 수 있었다.
    - 프로젝트 배경에 소개한 내용 처럼 기후 변화가 가시적으로 나타난 것을 확인하였다.

## 상관분석
### 다중공선성 진단
고구마 가격 데이터의 VIF 표

- 상관분석 결과
    - 경제지표와 시장지표에 대한 상관계수가 상대적으로 높게 나타났다.
        - 상관계수가 매우 높게 나타난 몇개의 피쳐를 다중공선성 진단하였다.
            - VIF(분산팽창지수)가 10 이상이면 다중공선성이 나타났다고 할 수 있는데,
            - VIF이 높게 나온 것을 확인하였다.
            - 따라서, 가격 예측에서 이 점을 고려하여 피쳐를 다르게 하여서도 진행하였다.
    - 주산지 기상데이터를 보면, 평균온도, 상대습도, 기상경보수를 제외한 피쳐들은 낮게 나타났다.

## 가격 예측

- ARIMA
    
    ```json
    'Product' : 'sweetpotato'
    'model' : 'ARIMA'
    
    'train_period' : (2005-03-01, 2018-12-31)
    'test_period' : (2019-01-01, 2020-12-31)
    
    'feature' : None 
    'params' : {'order':(2,1,2)}
    
    'mae': 1686.3337389771978,
    'mape': 0.18161889697068034,
    'mpe': 0.06382408151758624,
    'rmse': 2247.737892861377
    ```


- SARIMA
    
    ```json
    'Product' : 'sweetpotato'
    'model' : 'SARIMA'
    
    'train_period' : (2005-03-01, 2018-12-31)
    'test_period' : (2019-01-01, 2020-12-31)
    
    'feature' : None
    'params' : {'order' : (2,1,2), 'seasonal_order' : (2,1,2,12)}
    
    'mae': 1957.765975876936,
    'mape': 0.23180347388336564,
    'mpe': 0.18026576016309903,
    'rmse': 2300.495257431632
    ```
  
    
- SARIMAX
    - 'feature' : ['item_CPI', 'item_PPI','Food_Price_Index','Cereals_Price_Index', KRW_USD_EXR','Annual_Call_Rate']
        
        ```json
        'Product' : 'sweetpotato'
        'model' : 'SARIMAX'
        
        'train_period' : (2005-03-01, 2018-12-31)
        'test_period' : (2019-01-01, 2020-12-31)
        
        'feature' : [
        		'item_CPI', 'item_PPI','Food_Price_Index',
        		'Cereals_Price_Index', 'KRW_USD_EXR','Annual_Call_Rate'
        		]
        'params' : {'order' : (2,1,2), 'seasonal_order' : (2,1,2,12)}
        
        'mae': 1269.5931572147645,
        'mape': 0.14390671569052613,
        'mpe': 0.09871556426875837,
        'rmse': 1433.9650913579515
        ```
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e14c4d5a-d3b3-4974-8efc-5619abaf3e5c/Untitled.png)
        
    - 'feature' : ['item_CPI', 'item_PPI']
        
        ```json
        'Product' : 'sweetpotato'
        'model' : 'SARIMAX'
        
        'train_period' : (2005-03-01, 2018-12-31)
        'test_period' : (2019-01-01, 2020-12-31)
        
        'feature' : ['item_CPI', 'item_PPI']
        'params' : {'order' : (2,1,2), 'seasonal_order' : (2,1,2,12)}
        
        'mae': 1484.8134795760045,
        'mape': 0.1637971067149467,
        'mpe': 0.09627351306126664,
        'rmse': 1694.6071021018943
        ```
        
        
    - 'feature' : ['Food_Price_Index', 'Cereals_Price_Index', 'KRW_USD_EXR', 'Annual_Call_Rate']
        
        ```json
        'Product' : 'sweetpotato'
        'model' : 'SARIMAX'
        
        'train_period' : (2005-03-01, 2018-12-31)
        'test_period' : (2019-01-01, 2020-12-31)
        
        'feature' : [
        		'Food_Price_Index',
        		'Cereals_Price_Index',
        		'KRW_USD_EXR',
        		'Annual_Call_Rate',
        		]
        'params' : {'order' : (2,1,2),'seasonal_order' : (2,1,2,12)}
        
        'mae': 1693.74888916462,
        'mape': 0.1952173917905018,
        'mpe': 0.13255715546461877,
        'rmse': 2007.3517069655722
        ```
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7703adf-3fc9-40db-9030-5361517a285d/Untitled.png)
        
- Prophet
    - 'feature' : None
        
        ```json
        'Product' : 'sweetpotato'
        'model' : 'Prophet'
        
        'train_period' : (2005-03-01, 2018-12-31)
        'test_period' : (2019-01-01, 2020-12-31)
        
        'feature' : None
        'params' : {
        		changepoint_prior_scale = 0.5, 
        		holidays_prior_scale = 0.3,
        		n_changepoints = 100, 
        		seasonality_mode = 'multiplicative',
        		weekly_seasonality = True,
        		daily_seasonality = True,
        		yearly_seasonality = True,
        		interval_width=0.95
        		}
        
        'mae': 2111.783
        ```
        
        
    - 'feature' : ['DayAvg_Temperature', 'DayDiff_Temperature', 'DayAvg_RelativeHumidity', 'DaySum_Rainfall', 'DayAvg_WindSpeed', 'DaySum_Sunshine', 'Warning_Count']
        
        ```json
        'Product' : 'sweetpotato'
        'model' : 'Prophet'
        
        'train_period' : (2005-03-01, 2018-12-31)
        'test_period' : (2019-01-01, 2020-12-31)
        
        'feature' : [	
        		'DayAvg_Temperature', 
        		'DayDiff_Temperature', 
        		'DayAvg_RelativeHumidity', 
        		'DaySum_Rainfall',
        		'DayAvg_WindSpeed',
        		'DaySum_Sunshine',
        		'Warning_Count'
        		]
        'params' : {
        		changepoint_prior_scale = 0.5, 
        		holidays_prior_scale = 0.3, 
        		n_changepoints = 100, 
        		seasonality_mode = 'multiplicative', 
        		weekly_seasonality = True, 
        		daily_seasonality = True, 
        		yearly_seasonality = True, 
        		interval_width=0.95
        		}
        
        'mae': 1932.375
        ```
        
        

### 가격 예측 결과 - 고구마

| Model | Feature | MAE | MAPE | MPE | RMSE |
| --- | --- | --- | --- | --- | --- |
| ARIMA | None | 1686.333 | 0.181 | 0.063 | 2247.737 |
| SARIMA | None | 1957.765 | 0.231 | 0.180 | 2300.495 |
| SARIMAX | item_CPI
item_PPI
Food_Price_Index
Cereals_Price_Index
KRW_USD_EXR
Annual_Call_Rate | 1269.593 | 0.143 | 0.098 | 1433.965 |
| SARIMAX | item_CPI
item_PPI | 1484.813 | 0.163 | 0.096 | 1694.607 |
| SARIMAX | Food_Price_Index
Cereals_Price_Index
KRW_USD_EXR
Annual_Call_Rate | 1693.748 | 0.195 | 0.132 | 2007.351 |
| Prophet | None | 2111.783 |  |  |  |
| Prophet | DayAvg_Temperature
DayDiff_Temperature
DayAvg_RelativeHumidity
DaySum_Rainfall
DayAvg_WindSpeed
DaySum_Sunshine
Warning_Count | 1932.375 |  |  |  |

# 결론

## 분석 결과

- EDA
    - 가격의 변화와 주산지의 기후데이터를 보았을 때, 2011년 전후로 큰 차이를 확인하였다.
    - 이를 바탕으로 추가적으로 조사한 결과, [한석호&승준호(2011)](https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000104350)에서 이상기후에의한 생산량 감소로 인한 가격증가가 있었음을 알 수 있었다.
- 상관분석
    - 경제지표와 시장지표에 대한 상관계수가 상대적으로 높게 나타났다.
    - 주산지 기상데이터를 보면, 평균온도, 상대습도, 기상경보수를 제외한 피쳐들은 낮게 나타났다.
    - 상관계수가 매우 높게 나타난 몇개의 피쳐를 다중공선성 진단하였다.
        - VIF(분산팽창지수)가 10 이상이면 다중공선성이 나타났다고 할 수 있는데,
        - VIF이 높게 나온 것을 확인하였다.
        - 따라서, 가격 예측에서 이 점을 고려하여 피쳐를 다르게 하여서도 진행하였다.
- 가격 예측
    - ARIMA, SARIMA, SARIMAX, Prophet의 모델로 가격예측을 진행하였을 때
    - SARIMAX 모델로 품목의 물가지수와 국제가격지수 그리고 환율와 콜금리를 변수로 설정하였을 때, 가장 높은 예측성능을 보였다.

## 한계점

- 거래량 데이터의 부재
- 도메인 지식
- 가격 데이터 조정

# **Appendix**

## S**ource**

- [서울특별시 농수산식품공사](https://garak.co.kr/main/main.do)
- [KAMIS 농산물 유통정보](https://www.kamis.or.kr/customer/reference/openapi_list.do)
- [기상자료개방포털](https://data.kma.go.kr/cmmn/main.do)

## Reference

[국제곡물 가격 상승 원인과 2011년 국내물가 파급영향 | 국내연구자료 | KDI 경제정보센터](https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000104350)

[[안내] 2022 농넷 농산물 가격 변동률 예측 AI 경진대회](https://aifactory.space/competition/data/2091)

[[농정춘추] 식량안보와 식량주권](http://www.ikpnews.net/news/articleView.html?idxno=49373)

[2021 농산물 가격예측 AI 경진대회](https://dacon.io/competitions/official/235801/data)

[LSTM 네트워크를 활용한 농산물 가격 예측 모델](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002409099)

[](https://library.krei.re.kr/pyxis-api/1/digital-files/7d2409e9-ff04-40dc-b0e2-ab646709c70a)

## Tools

- Data Collecting
    - [Requests](https://requests.readthedocs.io/)
- Data Analytics
    - [Pandas](https://pandas.pydata.org/)
    - [Numpy](https://numpy.org/)
    - [statsmodels](https://www.statsmodels.org/)
- Data Visualization
    - [Matplotlib](https://matplotlib.org/)
    - [Seaborn](https://seaborn.pydata.org/)
    - [Tableau](https://www.tableau.com/)
- Machine Learning
    - [Prophet](https://facebook.github.io/prophet/)
- ETC
    - Team Collaboration Tool
        - Git
        - Github
        - Discord
        - Notion
    - Output Distribution
        - Google Slides
        - Streamlit

# 회고

- 배운점
    - 농산품 시장과 식량 안보에 대한 현황
    - 시계열 데이터의 특징
    - 시계열 예측 모델
        - `ARIMA` `SARIMA` `SARIMAX` `Prophet`
    - 다중공선성
- 프로젝트 한계점에 대한 회고
    - 거래량 데이터의 부재
        - 거래량 데이터는 시장에서 매우 중요하지만, API승인이 프로젝트 기간 내에 이루어 지지않아 불가피하게 활용하지 못하였다.
        - 프로젝트를 진행하면서 가장 당황스러운 일이었다. 앞으로도 이러한 일이 발생할 수 있을 것인데, 데이터 분석에서 데이터를 활용할 수 없는 상황일 때, 보간하거나 추정치를 활동하는 등의 방법이 있는 것으로 알지만, 앞으로 더 많은 프로젝트를 경험해보면서 개선하여 비슷한 상황이 왔을 때, 더 나은 결과를 낼 수 있을 것이다.
    - 도메인 지식
        - 농산품 시장은 다른 시장에 비해 변동성이 큰 시장
        - 작물의 특징, 기후, 경제, 문화, 외교 등 많은 요인에 영향을 받음
        - 위와 같은 이유로 농산품 시장에 대한 지식이 부족한 상태에서 진행한 프로젝트이므로 많은 부족함이 보임.
        - 이러한 부분을 개선하기 위해 프로젝트 진행 초반에 관련 현황에 대한 보고자료 등을 조사하여 팀원들과 공유하는 것이 좋을 것 같음.
    - 가격 데이터 조정
        - 본 프로젝트에서는 명목 가격으로만 분석 및 예측을 진행하였음.
        - 물가지수를 피쳐로 활용하기는 하였지만, 등락폭이나 실질 가격을 통하여 분석 및 예측을 해보았다면 더 좋은 프로젝트가 되었을 것임.
