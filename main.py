import argparse
from src.connector import connect
from src.portfolio import get_portfolio_summary, print_portfolio_summary

def run_summary():
    ib = connect()
    summary = get_portfolio_summary(ib)
    print_portfolio_summary(summary)
    ib.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IBKR Portfolio Analyzer")
    parser.add_argument("--summary", action="store_true", help="Show portfolio summary")
    args = parser.parse_args()

    if args.summary:
        run_summary()
    else:
        print("Use --summary to see your portfolio.")