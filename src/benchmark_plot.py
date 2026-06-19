import matplotlib.pyplot as plt

def plot_performance(returns, output_filepath="output/performance.png"):
    """
    Plots normalized cumulative returns for each ticker.
    """
    plt.figure(figsize=(10, 6))

    for column in returns.columns:
        plt.plot(returns.index, returns[column], label=column, linewidth=1.8)

    plt.axhline(y=100, color="gray", linestyle="--", linewidth=0.8, label="Starting point")
    plt.title("Portfolio vs Benchmark — Normalized Performance")
    plt.xlabel("Date")
    plt.ylabel("Value (Base 100)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_filepath)
    print(f"Chart saved to {output_filepath}")