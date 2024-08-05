import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas_ta as ta

# Download historical data
def download_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

# Calculate Bollinger Bands
def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    data['SMA'] = data['Close'].rolling(window).mean()
    data['BB_Upper'] = data['SMA'] + num_std_dev * data['Close'].rolling(window).std()
    data['BB_Lower'] = data['SMA'] - num_std_dev * data['Close'].rolling(window).std()
    return data

# Calculate Supertrend
def calculate_supertrend(data, atr_period=10, multiplier=3):
    supertrend = ta.supertrend(data['High'], data['Low'], data['Close'], length=atr_period, multiplier=multiplier)
    data = data.join(supertrend)
    return data

# Define the strategy
def strategy(data):
    data = calculate_bollinger_bands(data)
    data = calculate_supertrend(data)
    
    # Use correct column names from pandas_ta output
    data['Buy_Signal'] = np.where((data['Close'] < data['BB_Lower']) & (data['SUPERT_10_3.0'] == 1), 1, 0)
    data['Sell_Signal'] = np.where((data['Close'] > data['BB_Upper']) & (data['SUPERT_10_3.0'] == -1), 1, 0)
    
    return data

# Plot the data
def plot_data(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['BB_Upper'], label='BB Upper Band', linestyle='--')
    plt.plot(data['BB_Lower'], label='BB Lower Band', linestyle='--')
    plt.plot(data['SUPERT_10_3.0'], label='Supertrend', linestyle='-.')
    plt.scatter(data.index[data['Buy_Signal'] == 1], data['Close'][data['Buy_Signal'] == 1], marker='^', color='green', label='Buy Signal', alpha=1)
    plt.scatter(data.index[data['Sell_Signal'] == 1], data['Close'][data['Sell_Signal'] == 1], marker='v', color='red', label='Sell Signal', alpha=1)
    plt.title('Bollinger Bands and Supertrend Strategy BY Utso')
    plt.legend(loc='best')
    plt.show()

# Main function
def main():
    ticker = 'AAPL'
    start_date = '2018-01-01'
    end_date = '2024-01-01'
    data = download_data(ticker, start_date, end_date)
    data = strategy(data)
    plot_data(data)

if __name__ == "__main__":
    main()
