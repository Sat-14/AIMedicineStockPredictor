import random
import datetime
import pandas as pd
from faker import Faker
from pymongo import MongoClient
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import joblib

fake = Faker()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
sales_collection = db["sales_data"]
medicine_collection = db["medicine_stock"]

def generate_sales_data():
    sales_data = []
    for _ in range(3):
        sale_time = fake.date_time_between(start_date="-3M", end_date="now")
        temperature = round(random.uniform(0, 40), 1)
        quantity_sold = random.randint(10, 500)
        sales_data.append({
            "sale_time": sale_time.strftime("%Y-%m-%d %H:%M:%S"),
            "day_of_week": sale_time.weekday(),
            "month": sale_time.month,
            "temperature": temperature,
            "quantity_sold": quantity_sold
        })
    return sales_data
def generate_medicine_data(n):
    medicines = []
    sales_records = []
    for _ in range(n):
        medicine_name = fake.unique.word().capitalize()
        stock = random.randint(10, 1000)
        sales = generate_sales_data()
        total_sales_1 = sum(sale["quantity_sold"] for sale in sales[:1])
        total_sales_2 = sum(sale["quantity_sold"] for sale in sales[1:2])
        total_sales_3 = sum(sale["quantity_sold"] for sale in sales[2:])
        
        if total_sales_1 != 0:
            trend_percentage = ((total_sales_3 - total_sales_1) / total_sales_1) * 100
        else:
            trend_percentage = 0
        
        if total_sales_1 < total_sales_2 < total_sales_3:
            sales_trend = f"up ({trend_percentage:.2f}%)"
        elif total_sales_1 > total_sales_2 > total_sales_3:
            sales_trend = f"down ({trend_percentage:.2f}%)"
        else:
            sales_trend = "stable (0%)"

        medicine = {
            "medicine_name": medicine_name,
            "stock": stock,
            "sales_trend": sales_trend
        }
        medicines.append(medicine)
        for sale in sales:
            sales_records.append({"medicine_name": medicine_name, **sale})
    return medicines, sales_records
medicine_data, sales_data = generate_medicine_data(100)
medicine_collection.insert_many(medicine_data)
sales_collection.insert_many(sales_data)
print("random medicine records and sales data inserted into the database.")

