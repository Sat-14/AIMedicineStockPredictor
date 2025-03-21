# MediTrend AI - Predictive Analytics for Pharmaceutical Inventory Management

## Overview
MediTrend AI is an advanced AI-powered platform designed for pharmacies and medical suppliers. It predicts medicine demand based on past sales data, temperature, and seasonal trends, optimizing inventory management and improving supply chain efficiency.

## Features

### **Backend AI Algorithms Used**
- **RandomForestRegressor**: A tree-based ensemble model that helps in predicting stock levels based on past trends.
- **GradientBoostingRegressor**: Improves prediction accuracy by sequentially correcting previous errors.
- **XGBoost**: An optimized gradient boosting library that enhances performance and efficiency.
- **Voting Regressor**: Combines predictions from multiple models (RandomForest, GradientBoosting, and XGBoost) to improve overall accuracy.
- **StandardScaler**: Normalizes input features to ensure consistent scaling, improving model stability.



### **Backend (FastAPI & MongoDB)**
- **Sales Data Collection**: Records medicine sales with timestamps, temperature, and quantity sold.
- **Machine Learning Model**:
  - Uses **Voting Regressor** (RandomForest, GradientBoosting, XGBoost)
  - Standardizes data with **StandardScaler** for improved accuracy.
  - Predicts stock needs for the next 15 days.
- **Automatic Model Retraining**: Each time new sales data is added, the model is retrained.
- **FastAPI Endpoints**:
  - `POST /add_sale/` → Adds a new sale record and retrains the model.
  - `GET /predict_stock/{medicine_name}` → Predicts stock needs for a specific medicine.
- **Data Storage**: MongoDB stores both sales history and predicted stock levels.
- **CSV Export**: Extracts training data and saves it locally.

### **Frontend**
- **Modern UI using TailwindCSS**
- **Real-Time Analytics Dashboard**
- **Sales & Inventory Visualization using ApexCharts**
- **User-Friendly Stock Alerts**

## Installation & Setup
### **1. Clone the Repository**
```sh
 git clone https://github.com/your-repo/meditrend-ai.git
 cd meditrend-ai
```
### **2. Run the Setup Script**
```sh
 chmod +x start.sh
 ./start.sh
```
This script:
✅ Installs required dependencies
✅ Starts MongoDB
✅ Inserts sample sales data
✅ Trains the model
✅ Launches FastAPI server



## Using the Sales Data Endpoint
### **Adding Sales Data**
To add a new sale record and retrain the model, send a `POST` request to:
```
POST /add_sale/
```
#### **Request Format (JSON)**
```json
{
    "medicine_name": "Paracetamol",
    "quantity_sold": 100,
    "temperature": 25.5,
    "sale_time": "2025-03-21 14:30:00"
}
```
#### **Response Format (JSON)**
```json
{
    "message": "Sale data added successfully and model retrained."
}
```

## Future Enhancements
- **Integration with External APIs** (weather, disease trends, supplier data)
- **Advanced Time Series Forecasting** (LSTMs, ARIMA, Prophet)
- **User Authentication & Role-Based Access Control**
- **Mobile App Integration**
- **Expiry Date Alerts Via Email**
- **Live Stock Updates**
- **Historical Trend Analysis**
- **Inventory Management**
- **Integration with External APIs** (weather, disease trends, supplier data)
- **Advanced Time Series Forecasting** (LSTMs, ARIMA, Prophet)
- **User Authentication & Role-Based Access Control**
- **Mobile App Integration**

## Welcoming Contributors
We encourage developers to contribute to this project by adding new features, improving accuracy, or enhancing the frontend UI. Feel free to fork the repository, submit pull requests, or suggest new ideas.

## Contributors
- [MANASH CHANRAWAL]
- [Frontend Developer: Manash007-04](https://github.com/Manash007-04)
- [Backend Developer: Sat-14](https://github.com/Sat-14/AIMedicineStockPredictor/commits?author=Sat-14)
- [SATWIK RAI]

## License
MIT License

