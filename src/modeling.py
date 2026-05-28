import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error


def train_model(df: pd.DataFrame, target: str = "TotalClaims"):
    """Train a Gradient Boosting Regressor to predict the target.

    Parameters
    ----------
    df: pd.DataFrame
        Input dataframe containing features and the target column.
    target: str, optional
        Name of the target column. Defaults to "TotalClaims".
    """
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"Model MAE: {mae:.3f}")
    return model
