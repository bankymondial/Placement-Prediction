import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle

# Load the dataset
data = "https://raw.githubusercontent.com/bankymondial/Placement-Prediction/refs/heads/main/placementdata.csv"
df = pd.read_csv(data)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('/', '')

# Column transformations
df['extracurricularactivities'] = df['extracurricularactivities'].str.lower()
df['placementtraining'] = df['placementtraining'].str.lower()
df['placementstatus'] = df['placementstatus'].str.lower()

# Map categorical values to numerical values
df['extracurricularactivities'] = df['extracurricularactivities'].map({'no': 0, 'yes': 1})
df['placementtraining'] = df['placementtraining'].map({'no': 0, 'yes': 1})
df['placementstatus'] = df['placementstatus'].map({'notplaced': 0, 'placed': 1})

# Define important features
important_features = [
    'placementtraining', 'extracurricularactivities', 'aptitudetestscore', 
    'hsc_marks', 'softskillsrating'
]

# Split the data into features (X) and target (y)
X = df[important_features]
y = df['placementstatus']  # Target column

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Normalize the numerical columns using StandardScaler
numerical_cols = X.select_dtypes(include=['float64', 'int64']).columns
numerical_cols = numerical_cols.difference(['extracurricularactivities', 'placementtraining', 'placementstatus'])

scaler = StandardScaler()

X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_val[numerical_cols] = scaler.transform(X_val[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

# Train the logistic regression model
log_reg_important = LogisticRegression(random_state=42)
log_reg_important.fit(X_train, y_train)

# Save the trained model and scaler
with open('important_features_model.pkl', 'wb') as f_out:
    pickle.dump((log_reg_important, scaler), f_out)

print("Model trained and saved successfully.")
