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

### **3. Access the API**
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Future Enhancements
- **Integration with External APIs** (weather, disease trends, supplier data)
- **Advanced Time Series Forecasting** (LSTMs, ARIMA, Prophet)
- **User Authentication & Role-Based Access Control**
- **Mobile App Integration**

## Contributors
- [Your Name]
- [Frontend Developer: Manash007-04](https://github.com/Manash007-04)
- [Backend Developer: Sat-14](https://github.com/Sat-14/AIMedicineStockPredictor/commits?author=Sat-14)
- [Your Name]

## License
MIT License

