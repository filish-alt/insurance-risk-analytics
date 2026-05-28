import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import shap

def preprocess_and_split(df, target_col, categorical_features, numerical_features):
    df = df.dropna(subset=[target_col])
    X = df.drop(columns=[target_col])
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median'))])
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    X_train_clean = pd.DataFrame(preprocessor.fit_transform(X_train), columns=preprocessor.get_feature_names_out())
    X_test_clean = pd.DataFrame(preprocessor.transform(X_test), columns=preprocessor.get_feature_names_out())

    return X_train_clean, X_test_clean, y_train, y_test, preprocessor

def train_and_eval(X_train, X_test, y_train, y_test):
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'XGBoost': XGBRegressor(n_estimators=100, random_state=42)
    }
    
    results = {}
    best_model = None
    best_r2 = -float('inf')
    best_model_name = ""

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        r2 = r2_score(y_test, y_pred)
        results[name] = {'RMSE': rmse, 'R2': r2}
        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_model_name = name
    
    return results, best_model_name, best_model

def plot_shap(model, X_train):
    """
    Plots SHAP summary plot for the tree-based model.
    """
    try:
        explainer = shap.Explainer(model, X_train)
        shap_values = explainer(X_train, check_additivity=False)
        shap.summary_plot(shap_values, X_train, show=False)
        return True
    except Exception as e:
        print("SHAP failed:", e)
        return False
