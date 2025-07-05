#%%
import yfinance as yf
import pandas as pd
from datetime import timedelta
import re

"""
    load the raw data
    first we will be preparing the headlines data
    it should be in this format:
    Ticker,Headline,Date
    and after we are done here it should look like
    Ticker,Headline,Date,Close,1-D_returns,3-D_returns,5-D_returns

"""
df = pd.read_csv('D:/Stock Movement/data/raw_data/nifty_100_headlines.csv')
df["Date"] = pd.to_datetime(df["Date"]) 



def get_close(ticker, date):
    step_up = [0, 1, 3, 5]
    close_price = []
    used_dates = set()

    if ticker == "UNITDSPR":
        ticker = "UNITDSPR.BO"
    else:
        ticker = ticker + ".NS"

    for steps in step_up:
        temp_date = date + timedelta(days=steps)
        tries = 0
        while tries < 5:
            if temp_date in used_dates:
                temp_date += timedelta(days=1)
                tries += 1
                continue

            data = yf.download(ticker, start=temp_date, end=temp_date + timedelta(days=1), progress=False)
            if not data.empty:
                close_price.append(data["Close"].iloc[0])
                used_dates.add(temp_date)
                break
            else:
                temp_date += timedelta(days=1)
                tries += 1
        else:
            close_price.append(None)

    return pd.Series(close_price, index=["Close", "1-D_Close", "3-D_Close", "5-D_Close"])

df[["Close", "1-D_Close", "3-D_Close", "5-D_Close"]] = df.apply(lambda row: get_close(row["Ticker"], row["Date"]), axis=1)




print(len(df))

df.to_csv("D:\Stock Movement\data\raw_data\scores.csv", index=False)


# %%
import re
import pandas as pd


df = pd.read_csv("D:/Stock Movement/data/raw_data/scores.csv")
pattern = r"\d+\.\d+"

df["Close"] = df["Close"].apply(
    lambda x: re.search(pattern, str(x)).group() if re.search(pattern, str(x)) else None
).astype(float) 
df["1-D_Close"] = df["1-D_Close"].apply(
    lambda x: re.search(pattern, str(x)).group() if re.search(pattern, str(x)) else None
).astype(float) 
df["3-D_Close"] = df["3-D_Close"].apply(
    lambda x: re.search(pattern, str(x)).group() if re.search(pattern, str(x)) else None
).astype(float) 
df["5-D_Close"] = df["5-D_Close"].apply(
    lambda x: re.search(pattern, str(x)).group() if re.search(pattern, str(x)) else None
).astype(float) 



# %%

df["1d_return"] = (df["1-D_Close"] - df["Close"]) / df["Close"] * 100 
df["3d_return"] = (df["3-D_Close"] - df["Close"]) / df["Close"] * 100 
df["5d_return"] = (df["5-D_Close"] - df["Close"]) / df["Close"] * 100 
df.drop(columns=['1-D_Close','3-D_Close','5-D_Close'],inplace = True)

df.to_csv("D:\Stock Movement\data\datasets\dataset-first.csv")
