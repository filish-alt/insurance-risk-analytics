import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_summary(df: pd.DataFrame) -> None:
    """Print basic descriptive statistics and head of the DataFrame."""
    print(df.describe())
    print(df.head())

def plot_distribution(df: pd.DataFrame, column: str) -> None:
    """Histogram with KDE for a numeric column."""
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_categorical(df: pd.DataFrame, column: str) -> None:
    """Bar plot for a categorical column."""
    plt.figure(figsize=(8, 4))
    sns.countplot(y=column, data=df, order=df[column].value_counts().index)
    plt.title(f'Counts of {column}')
    plt.show()
