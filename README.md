Bollinger Bands and Supertrend Strategy

![Screenshot 2024-08-05 191902](https://github.com/user-attachments/assets/5f5262c3-b54b-47bf-8e1c-76f90e8f66f6)

Overview
This repository contains a Python script that implements a trading strategy using Bollinger Bands and Supertrend indicators. The strategy is designed to identify potential buy and sell signals for a given stock based on historical price data. This combination of technical indicators can help traders make informed decisions by highlighting periods of potential price breakouts or reversals.

Bollinger Bands
Bollinger Bands are a popular technical analysis tool invented by John Bollinger. They consist of three lines: a simple moving average (SMA) and two standard deviation lines, one above and one below the SMA. These bands expand and contract based on the volatility of the market. The upper and lower bands can indicate overbought or oversold conditions respectively:

Upper Band: SMA + (num_std_dev * standard deviation)
Lower Band: SMA - (num_std_dev * standard deviation)
Supertrend Indicator
The Supertrend indicator is another useful tool in technical analysis, primarily used to identify the direction of the trend and potential reversal points. It uses the Average True Range (ATR) to compute its values, and it plots a line above or below the price to signal a trend. The key parameters for the Supertrend indicator are the ATR period and the multiplier:

ATR Period: The number of periods over which the ATR is calculated.
Multiplier: The factor by which the ATR is multiplied to set the distance of the Supertrend line from the price.
Strategy Implementation
The strategy implemented in this script uses the following logic to generate buy and sell signals:

Buy Signal: Generated when the closing price crosses below the lower Bollinger Band and the Supertrend indicator signals an uptrend.
Sell Signal: Generated when the closing price crosses above the upper Bollinger Band and the Supertrend indicator signals a downtrend.
Script Overview
Dependencies
The script relies on several libraries, including pandas, numpy, yfinance, matplotlib, and pandas_ta. Ensure these libraries are installed using pip before running the script.

Functions
download_data(ticker, start, end): Downloads historical stock data for the given ticker symbol between the specified start and end dates using yfinance.
calculate_bollinger_bands(data, window=20, num_std_dev=2): Computes the Bollinger Bands for the given data.
calculate_supertrend(data, atr_period=10, multiplier=3): Computes the Supertrend indicator for the given data.
strategy(data): Combines the Bollinger Bands and Supertrend calculations to generate buy and sell signals.
plot_data(data): Plots the stock price, Bollinger Bands, Supertrend indicator, and buy/sell signals on a graph.
Main Function
The main function sets the stock ticker (e.g., 'AAPL' for Apple Inc.), start and end dates for the historical data, and runs the strategy:

python

def main():
    ticker = 'AAPL'
    start_date = '2021-01-01'
    end_date = '2022-01-01'
    data = download_data(ticker, start_date, end_date)
    data = strategy(data)
    plot_data(data)

    
Plotting
The script generates a plot showing:

The closing price of the stock.
The upper and lower Bollinger Bands.
The Supertrend line.
Buy signals marked with green upward triangles.
Sell signals marked with red downward triangles.
Conclusion
This trading strategy script provides a visual and analytical approach to trading using Bollinger Bands and the Supertrend indicator. By integrating these two powerful tools, traders can better understand market conditions and potentially improve their trading decisions. Feel free to modify the parameters and ticker symbol to suit your specific needs and explore different trading scenarios.

![Screenshot 2024-08-05 191952](https://github.com/user-attachments/assets/d0d18b1b-3dd4-432b-91d0-5b358c0550ff)
