import argparse
from src.connector import connect
from src.portfolio import get_portfolio_summary, print_portfolio_summary
from src.benchmark import get_historical_data, calculate_returns, print_performance_summary
from src.benchmark_plot import plot_performance
from src.projection import project_growth, print_projection
from src.portfolio import get_portfolio_summary, print_portfolio_summary, plot_distribution

def run_summary():
    ib = connect()
    summary = get_portfolio_summary(ib)
    print_portfolio_summary(summary)
    ib.disconnect()

    
def run_performance():
    tickers = ["IWDA.AS", "EIMI.L", "^GSPC"]
    data = get_historical_data(tickers)
    returns = calculate_returns(data)
    plot_performance(returns)
    print_performance_summary(returns)

def run_projection(monthly_contribution, annual_return, years):
    ib = connect()
    summary = get_portfolio_summary(ib)
    current_value = sum(item["market_value"] for item in summary)
    ib.disconnect()

    results = project_growth(current_value, monthly_contribution, annual_return, years)
    print_projection(results, current_value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IBKR Portfolio Analyzer")
    parser.add_argument("--summary", action="store_true", help="Show portfolio summary")
    parser.add_argument("--performance", action="store_true", help="Plot performance vs benchmark")
    parser.add_argument("--projection", action="store_true", help="Show growth projection")
    parser.add_argument("--monthly", type=float, default=300, help="Monthly contribution")
    parser.add_argument("--return-rate", type=float, default=0.07, help="Expected annual return (e.g. 0.07 for 7%%)")
    parser.add_argument("--years", type=int, default=20, help="Projection horizon in years")
    parser.add_argument("--distribution", action="store_true", help="Show portfolio distribution chart")
    args = parser.parse_args()

    if args.summary:
        run_summary()
    elif args.performance:
        run_performance()
    elif args.projection:
        run_projection(args.monthly, args.return_rate, args.years)
    elif args.distribution:
        ib = connect()
        summary = get_portfolio_summary(ib)
        plot_distribution(summary)
        ib.disconnect()
    else:
        print("Use --summary, --performance, --projection, or --distribution to run the respective analysis.")