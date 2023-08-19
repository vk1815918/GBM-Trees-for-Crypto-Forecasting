## TA indicators ##
import pandas as pd
import pandas_ta as ta

class Indicators:
    
    def overlays(data):
        # for i in range(2, 7, 2):                            
        # Apply only the indicators that can be turned into ratios with multiple lengths
        tem = data
        data.ta.bbands(length=20, std=2, append=True) # Bollinger Bands
        data.ta.dm(length=14, append=True) # Donchian Channel
        data.ta.kc(length=20, scalar=2, mamode='ema', offset=0, append=True) # Keltner Channel
        data.ta.midprice(append=True) # Median Price

        df_ratio = data.apply(lambda row: pd.Series({col + "_ratio": row[col] / row["Close"] for col in list(data)}), axis=1)
        df_ratio.drop(columns=['Volume_ratio', 'Close_ratio'])
        df_ratio = pd.concat([tem, df_ratio], axis=1)

        return df_ratio
    
    # Define some helper functions
    def sign(x):
        # Returns 1 if x is positive, -1 if x is negative and 0 if x is zero
        return x / abs(x) if x != 0 else 0

    def zscore(x):
        # Returns the standardized z-score of x
        return (x - x.mean()) / x.std()
            
    def oscilators(data):
        # for i in range(2, 7, 2):                            
        # Apply the rest of the indicators that are not suitable for ratio calculation with multiple lengths
        data.ta.obv(append=True) # On-Balance Volume
        data.ta.ad(append=True) # Accumulation/Distribution Index
        data.ta.atr(length=14, append=True) # Average True Range
        data.ta.natr(length=14, append=True) # Normalized Average True Range
        data.ta.true_range(append=True) # True Range
        data.ta.cmf(length=20, append=True) # Chaikin Money Flow
        data.ta.mfi(length=14, append=True) # Money Flow Index
        data.ta.nvi(append=True) # Negative Volume Index
        data.ta.massi(fast=9, slow=25, append=True) # Mass Index
        data.ta.cmo(length=9, append=True) # Chande Momentum Oscillator
        data.ta.cg(length=10, append=True) # Center of Gravity
        data.ta.rsi(length=14, append=True) # Relative Strength Index
        data.ta.apo(length=10, append=True) # Absolute Price Oscillator
        data.ta.bias(length=14, append=True) # Bias
        data.ta.bop(append=True) # Balance of Power
        data.ta.brar(length=13, append=True) # Bear and Bull Power
        data.ta.cci(length=20, append=True) # Commodity Channel Index
        data.ta.eom(length=14, append=True) # Ease of Movement
        data.ta.efi(length=13, append=True) # Force Index
        data.ta.macd(fast=12, slow=26, signal=9, append=True) # Moving Average Convergence Divergence
        data.ta.mom(length=10, append=True) # Momentum
        data.ta.ppo(length=10, append=True) # Percentage Price Oscillator
        data.ta.pvo(length=12, append=True) # Percentage Volume Oscillator
        data.ta.qstick(length=14, append=True) # Qstick
        data.ta.slope(length=20, append=True) # Slope
        data.ta.trix(length=18, append=True) # Triple Exponential Average
        data.ta.tsi(fast=25, slow=13, signal=13, append=True) # True Strength Index

        return data
