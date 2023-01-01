import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

def reduce_mem_usage(df, verbose=True):
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df


def envPath(dict_path=None):
    import platform
    from pprint import pprint

    global root_path
    global data_path

    dict_path_default = {
        "Windows": {"root_path": "../", "data_path": "data"},
        "Google_Colab": {
            "root_path": "../gdrive/Shareddrives/Agricultural Products Price Prediction/",
            "data_path": "data",
        },
        "Kaggle_notebook": {"root_path": "..", "data_path": "input"},
    }
    # 추후에 dict_path에 Kaggle_notebook이 없으면 추가하는 코드 추가 요망
    if dict_path != None:
        for k, v in dict_path.items():
            dict_path_default[k] = v

    dict_path = dict_path_default

    env = platform.uname().system

    if env == "Windows":
        env = env

    elif env == "Linux":
        import sys

        # Google_Colab
        if "google.colab" in sys.modules:
            env = "Google_Colab"
            from google.colab import drive

            drive.mount("/gdrive", force_remount=True)

        # Kaggle_notebook
        else:
            import os

            if list(os.walk("/kaggle/"))[0][1] == ["lib", "input", "working"]:
                env = "Kaggle_notebook"

    root_path = dict_path[env]["root_path"]
    data_path = f"{root_path}/{dict_path[env]['data_path']}"
    print("▣ env :", env)
    print()
    print("▣ platform.uname()", "\n", platform.uname(), sep="")
    print()
    print("▣ data_path", "\n", data_path, sep="")


class EDA:

    def __init__(
            self:pd.DataFrame,
            df,
            idx=None,
            x=None,
            y=None,
            fig_col_len=2,
            cheetkey=None,
            Product=None,
            ) -> pd.DataFrame:
        
        self.cheetkey = cheetkey

        if cheetkey == "Agri":
            if idx == None:
                idx == "YMD"

            if x == None:
                x = [
                    "KRW_USD_EXR",
                    "Annual_Call_Rate",
                    "item_PPI",
                    "item_CPI",
                    "Food_Price_Index",
                    "Cereals_Price_Index",
                    "DayAvg_Temperature",
                    "DayDiff_Temperature",
                    "DayAvg_RelativeHumidity",
                    "DaySum_Rainfall",
                    "DayAvg_WindSpeed",
                    "DaySum_Sunshine",
                    "Warning_Count",
                ]
            if y == None:
                y = "Price"

        elif cheetkey == "AgriMarket":
            if idx == None:
                idx == "YMD"

            if x == None:
                x = [
                    '환율(원/US$)',
                    '콜금리(연%)',
                    'item_PPI',
                    'item_CPI',
                    'Food Price Index',
                    'Cereals',
                ]

            if y == None:
                y = "Price"
    
        elif cheetkey == "AgriWeather":
            if idx == None:
                idx == "YMD"

            if x == None:
                x = [
                    'DayAvg_Temperature',
                    'DayDiff_Temperature',
                    'DayAvg_RelativeHumidity',
                    'DaySum_Rainfall',
                    'DayAvg_WindSpeed',
                    'DaySum_Sunshine',
                    'Warning_Count',
                ]
            if y == None:
                y = "DayAvg_Temperature"
        else:
            pass

        self.idx = idx
        if idx != None:
            temp = df.set_index(idx)
            self.df = temp
        else:
            self.df = df

        self.Product = Product
        if Product != None:
            self.df = df[df["Product"] == "마늘"]

        self.x = x
        self.y = y
        self.fig_col_len = fig_col_len

        # 로그 변환
        df_log1p = df.copy()
        for i in x:
            if min(df[i]) < 0:
                df_log1p[i] = np.log1p(df[i]-min(df[i]))
            else:
                df_log1p[i] = np.log1p(df[i])
        self.df_log1p = df_log1p

        # 로그변환 -> 로버스트스케일링
        from sklearn.preprocessing import RobustScaler
        transformer = RobustScaler().fit_transform(df_log1p[x])
        df_log1p_robSc = df_log1p.copy()
        df_log1p_robSc[x] = transformer
        self.df_log1p_robSc = df_log1p_robSc



    def print_title(body, br=2, bp="┌▣ ", hr=" ---- ---- ---- ----"):

        """
        body : 내용
        bp : bullet point, 글머리 기호
        hr : Horizontal Rule, 수평선
        """

        class ff:
            PURPLE = "\033[95m"
            CYAN = "\033[96m"
            DARKCYAN = "\033[36m"
            BLUE = "\033[94m"
            GREEN = "\033[92m"
            YELLOW = "\033[93m"
            RED = "\033[91m"
            BOLD = "\033[1m"
            UNDERLINE = "\033[4m"
            END = "\033[0m"

        print("\n" * br + ff.BOLD + bp + ff.UNDERLINE + body + ff.END + hr)
        

    def Check_df(df) -> pd.DataFrame:

        EDA.print_title("""df.shape""")
        print(df.shape)


        EDA.print_title("""df.info()""")
        print(df.info())

        EDA.print_title("""df.head()""")
        display(df.head())

        EDA.print_title("""df.columns.to_list()""")
        print(df.columns.to_list())

    def Check_self(self) -> pd.DataFrame:

        df = self.df
        # df_log1p = self.df_log1p
        # df_log1p_robSc = self.df_log1p_robSc

        EDA.print_title("""df.shape""")
        print(df.shape)

        EDA.print_title("""df.info()""")
        print(df.info())

        EDA.print_title("""df.head()""")
        display(df.head())

    def uv(self) -> None:

        df = self.df
        df_log1p = self.df_log1p
        df_log1p_robSc = self.df_log1p_robSc
        
        fig_col_len = self.fig_col_len
        import math
        fig_row_len = math.ceil(len(self.x) / fig_col_len)
        
        EDA.print_title("""df.describe().T""")
        display(df.describe().T)

        EDA.print_title("""df.describe(include=['O'])""")
        display(df.describe(include=["O"]))

        # 결측치
        df_temp = df.isna()
        EDA.print_title("""df.isna().sum()""")
        display(df_temp.sum().to_frame())

        EDA.print_title("""sns.heatmap(data=df.isna())""")
        sns.heatmap(data=df.isna(), cmap='Greys')
        plt.title("""sns.heatmap(data=df.isna())""", fontsize=20)
        plt.show()

        EDA.print_title("df.isna().mean()")
        display(df_temp.mean().to_frame())

        # 분포 - hist
        EDA.print_title("df.hist()")
        df[self.x].hist(bins=100, figsize=(20, 12))
        plt.show()
        # 로그 변환 후 분포
        EDA.print_title("df_log1p.hist()")
        df_log1p[self.x].hist(bins=100, figsize=(20, 12))
        plt.show()
        # 로그변환 -> 로버스트 스케일링 후 분포
        EDA.print_title("df_log1p_robSc.hist()")
        df_log1p_robSc[self.x].hist(bins=100, figsize=(20, 12))
        plt.show()

        for i in self.x:
            sns.violinplot(data=df, x=i)
            plt.title(f"df_{i}_violinplot", fontsize=16)
            plt.show()

        for i in self.x:
            sns.violinplot(data=df_log1p, x=i)
            plt.title(f"df_log1p_{i}_violinplot", fontsize=16)
            plt.show()
            
        for i in self.x:
            sns.violinplot(data=df_log1p_robSc, x=i)
            plt.title(f"df_log1p_robSc_{i}_violinplot", fontsize=16)
            plt.show()
        
        # 분포 - d, sns.displot(data=df_raw, x=df_raw.columns[7], kde=True)
        for i in self.x:
            sns.displot(data=df, x=i, kde=True)
            plt.title(f"df_{i}_displot", fontsize=16)
            plt.show()

        for i in self.x:
            sns.displot(data=df_log1p, x=i, kde=True)
            plt.title(f"df_log1p_{i}_displot", fontsize=16)
            plt.show()

        for i in self.x:
            sns.displot(data=df_log1p_robSc, x=i, kde=True)
            plt.title(f"df_log1p_robSc_{i}_displot", fontsize=16)
            plt.show()
        
        # # 수정 필요
        # df.pivot_table(index=self.idx, values=self.y).plot(figsize=(20, 8))
        # for i in self.x:
        #     df.pivot_table(index=self.idx, values=i).plot(figsize=(20, 8))



    def mv(self) -> None:

        df = self.df
        df_log1p = self.df_log1p
        df_log1p_robSc = self.df_log1p_robSc

        fig_col_len = self.fig_col_len
        import math
        fig_row_len = math.ceil(len(self.x) / fig_col_len)
        
        df_corr = df.corr()
        EDA.print_title("""df.corr()""")
        display(df_corr)
        EDA.print_title("""sns.heatmap(data=df.corr(), annot=True, fmt=".2f")""")
        plt.figure(figsize=(20,7))
        sns.heatmap(data=df_corr, annot=True, fmt=".2f", annot_kws={"size": 14})
        plt.show()
        
        if self.y != None:
            for i in self.x:
                sns.regplot(data=df, x=i, y=self.y)
                plt.show()
