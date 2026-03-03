# 🚗 Car MPG Predictor

A Machine Learning web application that predicts a car's fuel efficiency (**Miles Per Gallon - MPG**) based on its specifications. This project uses a **Linear Regression** model trained on the classic Auto MPG dataset.

## 🚀 Live Demo
[Paste your Streamlit deployment link here]

## 📊 Project Overview
The goal of this project is to estimate the mileage of a vehicle by analyzing features like:
- Cylinders
- Displacement
- Horsepower
- Weight
- Acceleration
- Model Year
- Origin (America, Europe, Asia)

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **ML Library:** Scikit-learn
- **Web Framework:** Streamlit
- **Data Handling:** Pandas & Numpy
- **Deployment:** Streamlit Cloud

## 📂 Folder Structure
```text
├── app.py                # Main Streamlit application script
├── car_model.pkl         # Trained Linear Regression model (Pickle file)
├── auto-mpg.csv          # Dataset used for training
├── requirements.txt      # List of dependencies for deployment
└── LinearReg.ipynb       # Jupyter Notebook with EDA and Model Training
