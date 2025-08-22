# Incedo Capstone Customer Intelligence API  
**Customer Intelligence Platform: Forecasting, Segmentation & Insight Dashboard**

## Objective
Develop a complete analytics platform that uses descriptive, predictive, and prescriptive analytics to understand customer behavior, forecast future outcomes, and support strategic decisions—deployed on a cloud platform.

## Business Use Case
The company wants to improve customer retention and marketing ROI by:
- Identifying key customer segments  
- Predicting future behavior  
- Visualizing insights for decision-makers  

This project integrates **machine learning models, customer segmentation, forecasting, and an interactive dashboard**.

---

## Project Structure

INCEDO-CAPSTONE/
│── data/ # Datasets
│ ├── customer_intelligence_dataset.csv
│ ├── customer_raw.csv
│ ├── customer_prepped.csv
│ ├── customer_scaled.csv
│ └── linear_reg_predictions.csv
│
│── models/ # Saved trained models
│ ├── kmeans_model.pkl
│ ├── linear_reg.pkl
│ ├── log_reg.pkl
│ └── random_forest.pkl
│
│── notebooks/ # Jupyter notebooks
│ ├── eda.ipynb
│ ├── feature_engineering.ipynb
│ ├── train_decisiontree.ipynb
│ ├── train_kmeans.ipynb
│ ├── train_linear_reg.ipynb
│ ├── train_logistic.ipynb
│ └── train_rf.ipynb
│
│── template/ # Flask app frontend
│ └── index.html
│── static/ # Stylesheets & assets
│ └── style.css
│
│── app.py # Flask API entrypoint
│── Dockerfile # Docker configuration
│── requirements.txt # Python dependencies
│── CustomerIntelligenceDashboard.pbix # Power BI dashboard
│── Capstone Project.pdf # Project documentation
│── README.md # Project guide (this file)

---

## 🤖 Machine Learning Models & Performance

### 1. **Decision Tree**
- ROC AUC: `0.634`  
- Accuracy: `0.614`  
- Strength: Simple interpretability  
- Limitation: Lower recall for minority class  

### 2. **K-Means (Segmentation)**
- Example clusters:  
  - k=8 → silhouette `0.528`  
  - k=16 → silhouette `0.419`  
- Best performing segmentation achieved at **k=8**.  

### 3. **Linear Regression**
- RMSE: `0.562`  
- MAE: `0.476`  
- R²: `0.945`  
- Strong performance for predicting **continuous variables (e.g., sales/forecasting)**.  

### 4. **Logistic Regression**
- Best C: `100`  
- Test Accuracy: `0.519`  
- ROC AUC: `0.515`  
- Limitation: Poor separation between classes.  

### 5. **Random Forest (Best Model)**
- Test Accuracy: `0.964`  
- ROC AUC: `0.992`  
- Precision (class 1): `0.98`  
- Recall (class 1): `0.86`  
- **Best overall performer**.  

### 🔑 Feature Importance (Top Drivers)
- `avg_order_value`, `days_since_last_purchase`, `age`, `tenure_months`  
- Frequency metrics (`freq_12m`, `freq_6m`, `freq_3m`)  
- Customer demographics (region, segment, gender)  

---

## 📊 Dashboard (Power BI)
An **interactive Power BI dashboard** provides:
- Customer segmentation views  
- Sentiment analysis  
- Purchase frequency & order value trends  
- Forecast vs actual performance  

---

## 🚀 Deployment Guide

### 1. Environment Setup
```bash
# Clone repo
git clone https://github.com/jaclynvu/incedo-capstone.git
cd incedo-capstone

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt

### 2. Run Flask App (locally)

export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=8080

### 3. Docker Deployment
# Build image
docker build -t customer-intel-api .

# Run container
docker run -p 8080:8080 customer-intel-api

### 4. Google Cloud Deployment

# Authenticate with Google Cloud SDK:

gcloud auth login
gcloud config set project <your_project_id>


#Push image to Artifact Registry:

docker tag customer-intel-api us-central1-docker.pkg.dev/<PROJECT_ID>/incedo-repo/customer-intel-api
docker push us-central1-docker.pkg.dev/<PROJECT_ID>/incedo-repo/customer-intel-api


#Deploy to Cloud Run:

gcloud run deploy customer-intel-api \
  --image us-central1-docker.pkg.dev/<PROJECT_ID>/incedo-repo/customer-intel-api \
  --platform managed --region us-central1 --allow-unauthenticated

