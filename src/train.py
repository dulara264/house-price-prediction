import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import joblib

from preprocess import preprocess_data

df = pd.read_csv("data/train.csv")

X, y, preprocessor = preprocess_data(df)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

model.fit(X, y)

preds = model.predict(X)
rmse = mean_squared_error(y, preds) ** 0.5


print("RMSE:", rmse)

joblib.dump(model, "models/house_price_model.pkl")
