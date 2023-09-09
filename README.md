# GBM-Trees-for-Crypto-Forecasting

In this repo, we use Gradient Boosted Trees for directional forecasting of the next minutely candlestick. It uses 60+ Technical indicators and using feature engineering standardizes the indicators to attain optimal parameters. The data used can be accessed and downloaded on the Binance historical data site which will be linked on the READ.ME file. 



DISCLAIMER: THIS REPOSITORY DOES NOT ENDORSE OR ADVOCATE ANY FINANCIAL PRODUCTS OR INVESTMENTS. THIS IS NOT INVESTMENT ADVICE. INVESTMENT AT YOUR OWN RISK.


![image](https://github.com/vk1815918/GBM-Trees-for-Crypto-Forecasting/assets/68977213/8ba51c69-726e-40e2-abaf-e1058b4869a1)


This is a overview of the Crypto_data_analysis file functions:

retrieve_btcusdt_file() retrieves the file which has the minutely bitcoin OHLCV data which you run this on.

I higly recommed you get this data from Binance Historical Data site: "https://www.binance.com/en/landing/data".

Go to the Kline option and download the SPOT option with whatever timeframe you want. 

Applyindicators simply get the indicators that are stored in the IndicatorImplementation.

ml is the funciton that splits the data for the GBM and runs it.

run_it is the function that compiles all the functions and runs them in order for you.


A good starting resource for learning about GBMs: https://en.wikipedia.org/wiki/Gradient_boosting


Introductory information about cryptocurrencies: https://www.bing.com/ck/a?!&&p=0795753fde7e833dJmltdHM9MTY5MjMxNjgwMCZpZ3VpZD0zNWI1N2M1OC04ODU3LTYxNTItM2NmYy02ZTk4ODlmYzYwNzMmaW5zaWQ9NTI3Mg&ptn=3&hsh=3&fclid=35b57c58-8857-6152-3cfc-6e9889fc6073&psq=cryptocurrency++and+trading+introuction&u=a1aHR0cHM6Ly93d3cuYnJpdGFubmljYS5jb20vbW9uZXkvd2hhdC1pcy1jcnlwdG9jdXJyZW5jeQ&ntb=1


![image](https://github.com/vk1815918/GBM-Trees-for-Crypto-Forecasting/assets/68977213/b11bf293-d541-4ce8-9f15-f3d30e923439)


