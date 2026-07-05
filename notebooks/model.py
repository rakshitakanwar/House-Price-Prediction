import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
# Current Working Directory
print("Current Directory:", os.getcwd())
# Load Dataset
df = pd.read_csv("data/House Price India.csv")
# Select Required Columns
df = df[[
    "living area",
    "number of bedrooms",
    "Postal Code",
    "Price"
]]
# Rename Column
df.rename(columns={
    "number of bedrooms": "Number of Rooms"}, inplace=True)
# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())
# Remove Missing Values
df.dropna(inplace=True)
# Features (Input)
X = df[[
    "living area",
    "Number of Rooms",
    "Postal Code"
]]

# Target (Output)
y = df["Price"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nModel Performance")
print("----------------------------")
print("R2 Score :", r2_score(y_test, y_pred))
print("MAE      :", mean_absolute_error(y_test, y_pred))

# Save Model
joblib.dump(model, "house_model.joblib")

print("\nModel Trained Successfully!")
print("Model saved as house_model.joblib")