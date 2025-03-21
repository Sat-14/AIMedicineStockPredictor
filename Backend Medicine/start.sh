#!/bin/bash

echo "Updating system and installing dependencies..."
sudo apt update && sudo apt install -y python3 python3-pip

echo "Installing required Python libraries..."
pip install --upgrade pip
pip install fastapi uvicorn pymongo joblib pandas scikit-learn xgboost faker

echo "Starting MongoDB (if not already running)..."
sudo systemctl start mongod || echo "MongoDB service not found. Ensure it's installed and running."

echo "Generating and inserting initial sales data..."
python learning.py

echo "Training the model..."
python model.py

echo "Starting FastAPI server..."
uvicorn fastapi_app:app --reload
