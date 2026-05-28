import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """\
# Exploratory Data Analysis - Insurance Risk Analytics
This notebook contains EDA covering data summarization, quality assessment, univariate/bivariate analysis, and geographic trends.
"""

code1 = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/insurance_data.csv')
display(df.head())
"""

code_summary = """\
# Data Summarization & Quality Assessment
print("Data Summary:")
display(df.describe())
print("\\nMissing Values:")
display(df.isnull().sum())

# Strategy for missing values:
# Drop rows with missing TotalPremium, and fill CustomValueEstimate with median.
df.dropna(subset=['TotalPremium'], inplace=True)
df['CustomValueEstimate'] = df['CustomValueEstimate'].fillna(df['CustomValueEstimate'].median())
"""

code_plots = """\
# Univariate Analysis & Outlier Detection
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df['TotalPremium'], bins=30, ax=axes[0], kde=True, color='skyblue')
axes[0].set_title('Distribution of Total Premium')

sns.boxplot(y=df['TotalClaims'], ax=axes[1], color='lightgreen')
axes[1].set_title('Outliers in Total Claims')

sns.countplot(data=df, x='VehicleType', ax=axes[2], palette='pastel')
axes[2].set_title('Vehicle Type Counts')

plt.tight_layout()
plt.show()
"""

code_bivariate = """\
# Bivariate / Multivariate Analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims', hue='Province', size='ClaimFrequency', sizes=(20, 200), alpha=0.7)
plt.title('Total Premium vs Total Claims by Province')
plt.show()
"""

code_geographic = """\
# Geographic Trends
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='Province', y='TotalPremium', hue='VehicleType', errorbar=None)
plt.title('Average Total Premium by Province and Vehicle Type')
plt.show()
"""

code_loss_ratio = """\
# Guiding Questions
# What is the overall Loss Ratio for the portfolio? How does it vary by Province, VehicleType, and Gender?
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
print("Overall Loss Ratio:", df['LossRatio'].mean())

print("\\nLoss Ratio by Province:")
display(df.groupby('Province')['LossRatio'].mean())
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_code_cell(code_summary),
    nbf.v4.new_code_cell(code_plots),
    nbf.v4.new_code_cell(code_bivariate),
    nbf.v4.new_code_cell(code_geographic),
    nbf.v4.new_code_cell(code_loss_ratio)
]

with open('notebooks/eda.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Notebook generated at notebooks/eda.ipynb")
