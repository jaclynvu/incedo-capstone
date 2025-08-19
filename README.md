# Iris ML Flask API

This project provides a RESTful API for predicting iris species and clustering using pre-trained machine learning models (Logistic Regression and KMeans) with Flask. It is ready for deployment on Google Cloud Run using Docker and Gunicorn.

## Features
- `/` : Health check endpoint
- `/predict` : POST endpoint for predictions
  - Request JSON: `{ "model_type": "logreg"|"kmeans", "features": [sepal_length, sepal_width, petal_length, petal_width] }`
  - Response: Model prediction

## Project Structure
```
app.py                # Main Flask app
models/               # Pre-trained model files (.pkl)
notebooks/            # Jupyter notebooks and data
requirements.txt      # Python dependencies
Dockerfile            # Container setup for Cloud Run
```

## Getting Started

### Local Development
1. Create and activate a Python 3 virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   flask run
   ```

### Docker
1. Build the Docker image:
   ```sh
   docker build -t iris-ml-flask .
   ```
2. Run the container:
   ```sh
   docker run -p 8080:8080 iris-ml-flask
   ```

### Google Cloud Run
- Deploy using the built Docker image. The app listens on port 8080 and uses Gunicorn for production.

## .gitignore
- Model files (`*.pkl`, `*.joblib`, `*.h5`), Python bytecode (`*.pyc`), and environment files are ignored.

## Example Request
```
POST /predict
Content-Type: application/json
{
  "model_type": "logreg",
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

## License
MIT
