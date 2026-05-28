import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 500

provinces = ['ON', 'BC', 'AB', 'QC']
genders = ['M', 'F', 'Other']
vehicle_makes = ['Toyota', 'Honda', 'Ford', 'Tesla', 'BMW']

data = {
    'ZipCode': np.random.randint(10000, 99999, size=n_rows).astype(str),
    'Province': np.random.choice(provinces, size=n_rows),
    'Gender': np.random.choice(genders, size=n_rows, p=[0.45, 0.45, 0.1]),
    'VehicleMake': np.random.choice(vehicle_makes, size=n_rows),
    'VehicleType': np.random.choice(['Sedan', 'SUV', 'Truck'], size=n_rows),
    'TotalPremium': np.round(np.random.normal(1500, 300, size=n_rows), 2),
    'TotalClaims': np.round(np.random.exponential(1000, size=n_rows), 2),
    'CustomValueEstimate': np.round(np.random.normal(30000, 10000, size=n_rows), 2),
    'ClaimFrequency': np.random.poisson(0.5, size=n_rows)
}

df = pd.DataFrame(data)

# Introduce some missing values
df.loc[np.random.choice(n_rows, 20, replace=False), 'CustomValueEstimate'] = np.nan
df.loc[np.random.choice(n_rows, 10, replace=False), 'TotalPremium'] = np.nan

df.to_csv('data/insurance_data.csv', index=False)
print("Mock dataset created with", n_rows, "rows at data/insurance_data.csv")
