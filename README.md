# GBM-Trees-for-Crypto-Forecasting
In this repo, we use Gradient Boosted Trees for directional forecasting of the next minutely candlestick. It uses 60+ Technical indicators and using feature engineering standardizes the indicators to attain optimal parameters. The data used can be accessed and downloaded on the Binance historical data site which will be linked on the READ.ME file. 



This is a overview of the Crypto_data_analysis file functions:

retrieve_btcusdt_file() retrieves the file which has the minutely bitcoin OHLCV data which you run this on.

I higly recommed you get this data from Binance Historical Data site: "https://www.binance.com/en/landing/data".

Go to the Kline option and download the SPOT option with whatever timeframe you want. 

Applyindicators simply get the indicators that are stored in the IndicatorImplementation.

ml is the funciton that splits the data for the GBM and runs it.

run_it is the function that compiles all the functions and runs them in order for you.
