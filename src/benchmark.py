import yfinance as yf
import pandas as pd

def get_historical_data(tickers, period="6mo"):
    """
    Downloads historical closing prices for a list of tickers.
    Returns a DataFrame with dates as index and tickers as columns.
    """
    data = yf.download(tickers, period=period)["Close"]
    return data


def calculate_returns(data):
    """
    Calculates cumulative percentage returns from the first available date.
    """
    normalized = (data / data.iloc[0]) * 100
    return normalized
def print_performance_summary(returns):
    """
    Prints the final return percentage for each ticker,
    using the last valid (non-NaN) value per column.
    """
    print("\n" + "="*40)
    print("PERFORMANCE SUMMARY (period total)")
    print("="*40)

    for ticker in returns.columns:
        last_valid_value = returns[ticker].dropna().iloc[-1]
        change = last_valid_value - 100
        sign = "+" if change >= 0 else ""
        print(f"{ticker:<10} | {sign}{change:.2f}%")

    print("="*40)