import nbformat as nbf

nb = nbf.v4.new_notebook()

md_intro = """\
# A/B Hypothesis Testing
In this notebook, we statistically validate key hypotheses about risk drivers to inform segmentation and pricing.
"""

code_data = """\
import pandas as pd
import sys
sys.path.append('../src')
from hypothesis_tests import test_categorical_kpi, test_numerical_kpi_multiple, test_numerical_kpi_two

df = pd.read_csv('../data/insurance_data.csv')

# KPIs
df['ClaimFrequencyFlag'] = (df['TotalClaims'] > 0).astype(int)
df['ClaimSeverity'] = df['TotalClaims']  # For records where TotalClaims > 0, which is most
df['Margin'] = df['TotalPremium'] - df['TotalClaims']

results = []
"""

code_h1 = """\
# H1: There are no risk differences across provinces. KPI: ClaimSeverity (ANOVA)
p_val, decision = test_numerical_kpi_multiple(df, 'Province', 'ClaimSeverity')
results.append({'Hypothesis': 'Provinces risk differences', 'Test': 'ANOVA', 'P-Value': p_val, 'Decision': decision})
print(f"H1 (Provinces vs Severity): p-value = {p_val:.4f} -> {decision}")
"""

code_h2 = """\
# H2: There are no risk differences between zip codes. KPI: ClaimFrequencyFlag (Chi-Squared)
p_val, decision = test_categorical_kpi(df, 'ZipCode', 'ClaimFrequencyFlag')
results.append({'Hypothesis': 'ZipCode risk differences', 'Test': 'Chi-Squared', 'P-Value': p_val, 'Decision': decision})
print(f"H2 (ZipCode vs Frequency): p-value = {p_val:.4f} -> {decision}")
"""

code_h3 = """\
# H3: There is no significant margin (profit) difference between zip codes. KPI: Margin (ANOVA)
p_val, decision = test_numerical_kpi_multiple(df, 'ZipCode', 'Margin')
results.append({'Hypothesis': 'ZipCode margin differences', 'Test': 'ANOVA', 'P-Value': p_val, 'Decision': decision})
print(f"H3 (ZipCode vs Margin): p-value = {p_val:.4f} -> {decision}")
"""

code_h4 = """\
# H4: There is no significant risk difference between Women and Men. KPI: ClaimSeverity (T-Test)
# Filter strictly Men and Women
df_gender = df[df['Gender'].isin(['M', 'F'])].copy()
p_val, decision = test_numerical_kpi_two(df_gender, 'Gender', 'ClaimSeverity')
results.append({'Hypothesis': 'Gender risk differences', 'Test': 'T-Test', 'P-Value': p_val, 'Decision': decision})
print(f"H4 (Gender vs Severity): p-value = {p_val:.4f} -> {decision}")
"""

code_summary = """\
import matplotlib.pyplot as plt
results_df = pd.DataFrame(results)
display(results_df)

print("\\n--- Business Interpretations ---")
for _, row in results_df.iterrows():
    if row['Decision'] == 'Reject H0':
        print(f"[REJECT H0]: We reject the null hypothesis for {row['Hypothesis']} (p = {row['P-Value']:.4f}). This indicates significant differences across this dimension, suggesting a targeted adjustment to our premiums is warranted for distinct subsets in this group.")
    else:
        print(f"[FAIL TO REJECT H0]: We fail to reject the null hypothesis for {row['Hypothesis']} (p = {row['P-Value']:.4f}). There is insufficient statistical evidence to say the risk varies, meaning our baseline pricing covers the underlying variance.")
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_intro),
    nbf.v4.new_code_cell(code_data),
    nbf.v4.new_code_cell(code_h1),
    nbf.v4.new_code_cell(code_h2),
    nbf.v4.new_code_cell(code_h3),
    nbf.v4.new_code_cell(code_h4),
    nbf.v4.new_code_cell(code_summary)
]

with open('notebooks/02_hypothesis_testing.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Generated Hypothesis notebook")
