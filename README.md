# AIMedicineStockPredictor
# MediTrend AI - Predictive Analytics for Pharmaceutical Inventory Management

## Overview
MediTrend AI is an advanced AI-powered platform designed for pharmacies and medical suppliers. It predicts medicine demand based on past sales data, temperature, and seasonal trends, optimizing inventory management and improving supply chain efficiency.

## Features

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



## Future Enhancements
- **Integration with External APIs** (weather, disease trends, supplier data)
- **Advanced Time Series Forecasting** (LSTMs, ARIMA, Prophet)
- **User Authentication & Role-Based Access Control**
- **Mobile App Integration**

## Contributors
- [Your Name]

## License
MIT License

