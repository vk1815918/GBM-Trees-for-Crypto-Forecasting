import pandas as pd
import numpy as np
import IndicatorImplementation as ii
import matplotlib.pyplot as plt
# import mplfinance as fplt
import yfinance as yf
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report


class crypto_data_analysis:

    def retrieve_btcusdt_file():
        print("in retrieve_btcusdt_file")
        btcusdt = pd.read_csv(r"C:\Users\vkotr\Python Projects\FinancialProjects\Crypto Trading\btcusdt.csv", index_col=0)
        btcusdt.rename(columns={btcusdt.columns[0]: 'dates'}, inplace=True)
        btcusdt['dates'] = pd.to_datetime(btcusdt['dates'])
        btcusdt.set_index('dates', inplace=True)
        btcusdt.drop('Close Time', axis=1, inplace=True)

        # btcusdt = btcusdt.resample('D').agg({
        #     'Open': 'first',
        #     'High': 'max',
        #     'Low': 'min',
        #     'Close': 'last',
        #     'Volume': 'sum'
        # })

        btcusdt = btcusdt.iloc[:10000]

        return btcusdt
    
    def applyIndicators(data):
        print("in applyIndicators")

        data = data.iloc[:,0:5]

        data = ii.Indicators.overlays(data=data)
        data = ii.Indicators.oscilators(data=data)

        return data

    def correlation(data):
        # data = pd.DataFrame()

        corr_matrix = data.corr()

        # Fill the diagonal elements with zero
        np.fill_diagonal(corr_matrix.values, 0)

        print(corr_matrix)
        print(corr_matrix['Close'])

        inverse_corr = corr_matrix['Close'].loc[corr_matrix['Close'] < 0].index
        corr = corr_matrix['Close'].loc[corr_matrix['Close'] > 0.2].index

        # Get a one-dimensional array of the correlation coefficients
        corr_array = corr_matrix.values.flatten()

        # # Plot the histogram of the correlation coefficients
        # plt.hist(corr_array, bins=1000)

        # # Add a title and labels
        # plt.title("Histogram of Correlation Coefficients")
        # plt.xlabel("Correlation Coefficient")
        # plt.ylabel("Frequency")

        # # Show the plot
        # plt.show()

        return inverse_corr.values, corr.values

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

        # inv, corr = crypto_data_analysis.correlation(df)

        df.dropna(inplace=True, axis=0)

        crypto_data_analysis.ml(df)

        # print(df)

crypto_data_analysis.run_it()
    

'''

Put all the techincal indicators like last time.

add the on-chain data

and then do a df.corr

and do extremes, most corr uncorr

see how they work out


'''