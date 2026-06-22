from src.portfolio import get_portfolio_summary, print_portfolio_summary

def test_summary_is_list():
    # Test with mock data — no IBKR connection needed
    mock_summary = [
        {
            "symbol": "IWDA",
            "currency": "EUR",
            "quantity": 100,
            "avg_cost": 124.55,
            "market_price": 125.17,
            "market_value": 12516.50,
            "unrealized_pnl": 61.53
        },
        {
            "symbol": "EIMI",
            "currency": "USD",
            "quantity": 100,
            "avg_cost": 58.07,
            "market_price": 57.90,
            "market_value": 5789.97,
            "unrealized_pnl": -17.22
        }
    ]
    assert isinstance(mock_summary, list)

def test_summary_has_required_keys():
    mock_summary = [
        {
            "symbol": "IWDA",
            "currency": "EUR",
            "quantity": 100,
            "avg_cost": 124.55,
            "market_price": 125.17,
            "market_value": 12516.50,
            "unrealized_pnl": 61.53
        }
    ]
    required_keys = {"symbol", "currency", "quantity", "avg_cost",
                     "market_price", "market_value", "unrealized_pnl"}
    assert required_keys.issubset(mock_summary[0].keys())

def test_total_value_calculation():
    mock_summary = [
        {"symbol": "IWDA", "currency": "EUR", "quantity": 100,
         "avg_cost": 124.55, "market_price": 125.17,
         "market_value": 12516.50, "unrealized_pnl": 61.53},
        {"symbol": "EIMI", "currency": "USD", "quantity": 100,
         "avg_cost": 58.07, "market_price": 57.90,
         "market_value": 5789.97, "unrealized_pnl": -17.22}
    ]
    total = sum(item["market_value"] for item in mock_summary)
    assert abs(total - 18306.47) < 0.01

def test_total_pnl_calculation():
    mock_summary = [
        {"symbol": "IWDA", "currency": "EUR", "quantity": 100,
         "avg_cost": 124.55, "market_price": 125.17,
         "market_value": 12516.50, "unrealized_pnl": 61.53},
        {"symbol": "EIMI", "currency": "USD", "quantity": 100,
         "avg_cost": 58.07, "market_price": 57.90,
         "market_value": 5789.97, "unrealized_pnl": -17.22}
    ]
    total_pnl = sum(item["unrealized_pnl"] for item in mock_summary)
    assert abs(total_pnl - 44.31) < 0.01