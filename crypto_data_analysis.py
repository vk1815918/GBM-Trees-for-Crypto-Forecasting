import pandas as pd
import numpy as np
import IndicatorImplementation as ii
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report


class crypto_data_analysis:

    def retrieve_btcusdt_file():
        print("in retrieve_btcusdt_file")
        btcusdt = pd.read_csv(r"PUT_YOUR_FILE_PATH_HERE", index_col=0)
        btcusdt.rename(columns={btcusdt.columns[0]: 'dates'}, inplace=True)
        btcusdt['dates'] = pd.to_datetime(btcusdt['dates'])
        btcusdt.set_index('dates', inplace=True)
        btcusdt.drop('Close Time', axis=1, inplace=True)

        btcusdt = btcusdt.iloc[:10000] # This is just to make the process run faster. You can run the whole dataset if you would like.

        return btcusdt
    
    def applyIndicators(data):
        print("in applyIndicators")

        data = data.iloc[:,0:5]

        data = ii.Indicators.overlays(data=data)
        data = ii.Indicators.oscilators(data=data)

        return data

    def ml(df):
        df["target"] = (df["Close"] < df["Close"].shift(-1)).astype(int)

        X = df.drop(columns=['target'], inplace=False)
        Y = df['target']

        split = int(len(df)*0.8) ### 80% train 20% test

        X_Train = X.iloc[:split]
        X_Test = X.iloc[split:]

        Y_Train = Y.iloc[:split]
        Y_Test = Y.iloc[split:]

        clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.01, max_depth=5, random_state=42)

        clf = clf.fit(X_Train, Y_Train)
        Y_pred = clf.predict(X_Test)

        print(classification_report(Y_Test, Y_pred))

    def run_it():
        print("in run_it")

        df = crypto_data_analysis.retrieve_btcusdt_file()

        df = crypto_data_analysis.applyIndicators(df)

        df.dropna(inplace=True, axis=0)

        crypto_data_analysis.ml(df)


crypto_data_analysis.run_it()
    

'''


This is the file which houses the main functions. A brief explanation of what the functions do: retrieve_btcusdt_file() 

retrieves the file which has the minutely bitcoin OHLCV data which you run this on. I higly recommed you get this data from

Binance Historical Data site: "https://www.binance.com/en/landing/data". Go to the Kline option and download the SPOT option 

with whatever timeframe you want. 


Applyindicators simply get the indicators that are stored in the IndicatorImplementation.

ml is the funciton that splits the data for the GBM and runs it.

run_it is the function that compiles all the functions and runs them in order for you.


'''
