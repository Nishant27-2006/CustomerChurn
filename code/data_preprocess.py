import pandas as pd

# Load the dataset
file_path = 'data.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Convert TotalCharges to numeric, coercing errors to handle non-numeric values
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

# Impute missing TotalCharges values with the median (since there may be some missing)
data['TotalCharges'].fillna(data['TotalCharges'].median(), inplace=True)

# Encode categorical variables: Binary columns using label encoding, others using one-hot encoding
data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})  # Label encoding for the target variable

# Identify categorical columns that are not binary
categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('customerID')  # Exclude customerID as it's just an identifier

# One-hot encode the remaining categorical variables
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Save the preprocessed data to a new CSV file
processed_file_path = 'processed_telco_customer_churn.csv'
data.to_csv(processed_file_path, index=False)

print(f"Processed data saved to {processed_file_path}")
