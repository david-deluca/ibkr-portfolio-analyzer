def get_portfolio_summary(ib):
    """
    Returns a list of position dicts enriched with market value and P&L.
    """
    portfolio_items = ib.portfolio()
    summary = []
    for item in portfolio_items:
        summary.append({
            "symbol": item.contract.symbol,
            "currency": item.contract.currency,
            "quantity": item.position,
            "avg_cost": round(item.averageCost, 2),
            "market_price": round(item.marketPrice, 2),
            "market_value": round(item.marketValue, 2),
            "unrealized_pnl": round(item.unrealizedPNL, 2)
        })
    return summary


def print_portfolio_summary(summary):
    """
    Prints a formatted table of the portfolio summary.
    """
    print("\n" + "="*70)
    print("PORTFOLIO SUMMARY")
    print("="*70)
    print(f"{'Symbol':<8} | {'Qty':>6} | {'Avg Cost':>9} | {'Price':>8} | {'Value':>10} | {'P&L':>8}")
    print("-"*70)

    total_value = 0
    total_pnl = 0
    for item in summary:
        print(f"{item['symbol']:<8} | {item['quantity']:>6} | {item['avg_cost']:>9} | "
              f"{item['market_price']:>8} | {item['market_value']:>10} | {item['unrealized_pnl']:>8}")
        total_value += item['market_value']
        total_pnl += item['unrealized_pnl']

    print("-"*70)
    print(f"{'TOTAL':<8} | {'':>6} | {'':>9} | {'':>8} | {total_value:>10.2f} | {total_pnl:>8.2f}")
    print("="*70)