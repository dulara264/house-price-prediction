import pandas as pd
import joblib

model = joblib.load("models/house_price_model.pkl")

df = pd.read_csv("data/test.csv")

predictions = model.predict(df)

for i, price in enumerate(predictions[:5], 1):
    print(f"House {i} predicted price: {price:.2f}")
