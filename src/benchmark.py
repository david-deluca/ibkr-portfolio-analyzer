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