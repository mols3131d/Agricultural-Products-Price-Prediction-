def reduce_mem_usage(df, verbose=True):
    import numpy as np
    import pandas as pd

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
