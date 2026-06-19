import argparse
from src.connector import connect
from src.portfolio import get_portfolio_summary, print_portfolio_summary
from src.benchmark import get_historical_data, calculate_returns, print_performance_summary
from src.benchmark_plot import plot_performance
from src.projection import project_growth, print_projection

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

def run_projection():
    current_value = 18192.48  # from your last --summary total
    monthly_contribution = 300
    annual_return = 0.07
    years = 20

    results = project_growth(current_value, monthly_contribution, annual_return, years)
    print_projection(results, current_value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IBKR Portfolio Analyzer")
    parser.add_argument("--summary", action="store_true", help="Show portfolio summary")
    parser.add_argument("--performance", action="store_true", help="Plot performance vs benchmark")
    parser.add_argument("--projection", action="store_true", help="Show growth projection")
    args = parser.parse_args()

    if args.summary:
        run_summary()
    elif args.performance:
        run_performance()
    elif args.projection:
        run_projection()
    else:
        print("Use --summary, --performance, or --projection to run the respective analysis.")