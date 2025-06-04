import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv("data/titanic.csv")

# ---- Missing Values ----
print("=== Missing Data ===")
missing = df.isnull().mean() * 100
missing = missing[missing > 0]
print(missing.round(2))

# ---- Outlier Detection ----
print("\n=== Outlier Detection ===")
numeric_df = df.select_dtypes(include='number').dropna()
iso = IsolationForest(contamination=0.1, random_state=42)
outliers = iso.fit_predict(numeric_df)
num_outliers = (outliers == -1).sum()
print(f"Number of outliers: {num_outliers}")

# ---- Dummy AI Summary ----
print("\n=== AI Summary ===")
print("The dataset has missing values in key columns and a moderate number of outliers.")
