import joblib
import pandas as pd

# Load model
model = joblib.load("house_model.joblib")

# User Input
data = pd.DataFrame({
    "living area": [2500],
    "Number of Rooms": [4],
    "Postal Code": [122004]
})



print(data)
prediction = model.predict(data)
print(prediction)
prediction = model.predict(data)

print("Predicted House Price:", prediction[0])