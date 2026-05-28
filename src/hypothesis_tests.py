import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, ttest_ind

def test_categorical_kpi(df, group_col, target_col):
    """
    Use Chi-Squared test for categorical KPIs (e.g., ClaimFrequencyFlag (0 or 1)).
    """
    contingency_table = pd.crosstab(df[group_col], df[target_col])
    chi2, p_val, dof, expected = chi2_contingency(contingency_table)
    decision = "Reject H0" if p_val < 0.05 else "Fail to reject H0"
    return p_val, decision

def test_numerical_kpi_multiple(df, group_col, target_col):
    """
    Use ANOVA for numerical KPIs across groups (e.g. ClaimSeverity, Margin).
    """
    groups = [group[target_col].dropna().values for name, group in df.groupby(group_col)]
    # Filter out empty groups if any
    groups = [g for g in groups if len(g) > 0]
    if len(groups) < 2:
        return 1.0, "Fail to reject H0"
    F, p_val = f_oneway(*groups)
    decision = "Reject H0" if p_val < 0.05 else "Fail to reject H0"
    return p_val, decision

def test_numerical_kpi_two(df, group_col, target_col):
    """
    Use T-test for numerical KPIs across exactly 2 groups (e.g. Gender).
    """
    groups = [group[target_col].dropna().values for name, group in df.groupby(group_col)]
    if len(groups) >= 2:
        stat, p_val = ttest_ind(groups[0], groups[1], equal_var=False)
        decision = "Reject H0" if p_val < 0.05 else "Fail to reject H0"
        return p_val, decision
    return 1.0, "Fail to reject H0"
