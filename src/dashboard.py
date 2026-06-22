import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from src.benchmark import get_historical_data, calculate_returns
from src.projection import project_growth

def plot_dashboard(summary, output_filepath="output/dashboard.png"):
    """
    Generates a 2x2 dashboard with portfolio summary, distribution,
    performance vs benchmark, and growth projection.
    """
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle("Portfolio Dashboard", fontsize=16, fontweight="bold", y=0.98)
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)

    # ── Panel 1 (top-left): Portfolio summary table ──
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.axis("off")
    ax1.set_title("Portfolio Summary", fontweight="bold")

    col_labels = ["Symbol", "Qty", "Avg Cost", "Price", "Value", "P&L"]
    table_data = [
        [
            item["symbol"],
            int(item["quantity"]),
            f"{item['avg_cost']:.2f}",
            f"{item['market_price']:.2f}",
            f"{item['market_value']:.2f}",
            f"{item['unrealized_pnl']:.2f}"
        ]
        for item in summary
    ]
    total_value = sum(item["market_value"] for item in summary)
    total_pnl = sum(item["unrealized_pnl"] for item in summary)
    table_data.append(["TOTAL", "", "", "", f"{total_value:.2f}", f"{total_pnl:.2f}"])

    table = ax1.table(
        cellText=table_data,
        colLabels=col_labels,
        loc="center",
        cellLoc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)

    # ── Panel 2 (top-right): Pie chart ──
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title("Distribution by Market Value", fontweight="bold")
    labels = [item["symbol"] for item in summary]
    values = [item["market_value"] for item in summary]
    ax2.pie(values, labels=labels, autopct="%1.1f%%", startangle=90,
            wedgeprops={"edgecolor": "white", "linewidth": 1.5})

    # ── Panel 3 (bottom-left): Performance vs benchmark ──
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_title("Performance vs Benchmark (6mo)", fontweight="bold")
    tickers = ["IWDA.AS", "EIMI.L", "^GSPC"]
    data = get_historical_data(tickers)
    returns = calculate_returns(data)
    for column in returns.columns:
        ax3.plot(returns.index, returns[column], label=column, linewidth=1.5)
    ax3.axhline(y=100, color="gray", linestyle="--", linewidth=0.8)
    ax3.set_ylabel("Value (Base 100)")
    ax3.legend(fontsize=8)
    ax3.grid(alpha=0.3)
    ax3.tick_params(axis="x", rotation=45)

    # ── Panel 4 (bottom-right): Projection ──
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_title("Growth Projection (20yr, 7%, 300€/mo)", fontweight="bold")
    results = project_growth(total_value, 300, 0.07, 20)
    years = [r[0] for r in results]
    values_proj = [r[1] for r in results]
    ax4.plot(years, values_proj, color="steelblue", linewidth=2)
    ax4.fill_between(years, values_proj, alpha=0.2, color="steelblue")
    ax4.axhline(y=total_value, color="gray", linestyle="--", linewidth=0.8, label="Current value")
    ax4.set_xlabel("Years")
    ax4.set_ylabel("Projected Value (€)")
    ax4.legend(fontsize=8)
    ax4.grid(alpha=0.3)

    plt.savefig(output_filepath, dpi=150, bbox_inches="tight")
    print(f"Dashboard saved to {output_filepath}")