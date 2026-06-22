import pandas as pd
from src.benchmark import get_historical_data, calculate_returns

def test_download_returns_dataframe():
    data = get_historical_data(["IWDA.AS"], period="1mo")
    assert isinstance(data, pd.DataFrame)

def test_download_not_empty():
    data = get_historical_data(["IWDA.AS"], period="1mo")
    assert len(data) > 0

def test_calculate_returns_starts_at_100():
    data = get_historical_data(["IWDA.AS"], period="1mo")
    returns = calculate_returns(data)
    first_value = returns.iloc[0]["IWDA.AS"]
    assert abs(first_value - 100) < 0.01

def test_calculate_returns_same_shape():
    data = get_historical_data(["IWDA.AS", "EIMI.L"], period="1mo")
    returns = calculate_returns(data)
    assert returns.shape == data.shape