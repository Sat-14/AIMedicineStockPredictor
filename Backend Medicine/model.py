
import random
import datetime
import pandas as pd
from faker import Faker
from pymongo import MongoClient
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
import xgboost as xgb
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

from learning import*
def train_stock_prediction_model():
    data = list(sales_collection.find())
    df = pd.DataFrame(data)
    
    if df.empty:
        return
    
    df["avg_sales"] = df.groupby("medicine_name")["quantity_sold"].transform("mean")
    df["sales_trend"] = df.groupby("medicine_name")["quantity_sold"].diff().fillna(0).apply(lambda x: 1 if x > 0 else -1)
    
    X = df[["avg_sales", "sales_trend", "day_of_week", "month", "temperature"]]
    y = df["quantity_sold"]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
    xg = xgb.XGBRegressor(n_estimators=100, random_state=42)
    
    ensemble = VotingRegressor([('rf', rf), ('gb', gb), ('xg', xg)])
    ensemble.fit(X_scaled, y)
    
    joblib.dump((scaler, ensemble), "stock_prediction_model.pkl")
    predictions = ensemble.predict(X_scaled).astype(int)
    df["predicted_stock_needs"] = predictions
    
    for _, row in df.iterrows():
        medicine_collection.update_one({"medicine_name": row["medicine_name"]}, {"$set": {"predicted_stock_needs": row["predicted_stock_needs"]}}, upsert=True)

train_stock_prediction_model()
print("Stock prediction model trained and predictions saved.")

