def project_growth(current_value, monthly_contribution, annual_return, years):
    """
    Projects portfolio growth using compound interest with monthly contributions.
    Returns a list of (year, value) tuples.
    """
    monthly_rate = annual_return / 12
    months = years * 12
    value = current_value
    results = []

    for month in range(1, months + 1):
        value = value * (1 + monthly_rate) + monthly_contribution
        if month % 12 == 0:
            results.append((month // 12, round(value, 2)))

    return results


def print_projection(results, current_value):
    """
    Prints a formatted table of projected portfolio growth.
    """
    print("\n" + "="*40)
    print(f"GROWTH PROJECTION (starting from {current_value:.2f})")
    print("="*40)
    print(f"{'Year':<6} | {'Projected Value':>16}")
    print("-"*40)

    for year, value in results:
        print(f"{year:<6} | {value:>16,.2f}")

    print("="*40)