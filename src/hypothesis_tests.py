import pandas as pd
from scipy import stats


def test_mean_difference(df: pd.DataFrame, column: str, group_col: str, group_a, group_b, alpha: float = 0.05):
    """Two‑sample t‑test for mean difference between two groups.
    """
    a = df.loc[df[group_col] == group_a, column].dropna()
    b = df.loc[df[group_col] == group_b, column].dropna()
    t_stat, p_val = stats.ttest_ind(a, b, equal_var=False)
    print(f"t={t_stat:.3f}, p={p_val:.4f}")
    if p_val < alpha:
        print("Reject null hypothesis: significant difference.")
    else:
        print("Fail to reject null hypothesis.")
