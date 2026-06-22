from src.projection import project_growth

def test_growth_increases_over_time():
    results = project_growth(10000, 300, 0.07, 10)
    values = [r[1] for r in results]
    assert values[-1] > values[0]

def test_growth_returns_correct_years():
    results = project_growth(10000, 300, 0.07, 10)
    assert len(results) == 10
    assert results[-1][0] == 10

def test_zero_contribution_still_grows():
    results = project_growth(10000, 0, 0.07, 5)
    values = [r[1] for r in results]
    assert values[-1] > 10000

def test_zero_return_only_contributions():
    results = project_growth(0, 100, 0.0, 1)
    final_value = results[-1][1]
    assert abs(final_value - 1200) < 1  # 100€ x 12 meses = 1200€