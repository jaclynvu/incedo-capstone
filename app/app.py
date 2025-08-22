from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load models
models = {
    "linear_reg": pickle.load(open("models/linear_reg.pkl", "rb")),
    "logistic_reg": pickle.load(open("models/log_reg.pkl", "rb")),
    "decision_tree": pickle.load(open("models/decision_tree.pkl", "rb")),
    "random_forest": pickle.load(open("models/random_forest.pkl", "rb")),
    "kmeans": pickle.load(open("models/kmeans_model.pkl", "rb"))
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict/<model_name>", methods=["POST"])
def predict(model_name):
    if model_name not in models:
        return jsonify({"error": f"Model '{model_name}' not found"}), 400

    data = request.json.get("features")
    if data is None:
        return jsonify({"error": "Request must contain 'features'"}), 400

    model = models[model_name]

    try:
        features = np.array(data).reshape(1, -1)
        prediction = model.predict(features)

        # Handle regression vs classification vs clustering
        if model_name in ["linear_reg", "random_forest", "decision_tree"]:
            result = float(prediction[0])  # regression output
        elif model_name in ["logistic_reg"]:
            result = int(prediction[0])    # classification output
        elif model_name == "kmeans":
            result = int(prediction[0])    # cluster label
        else:
            result = str(prediction[0])

        return jsonify({
            "model_name": model_name,
            "features": features,
            "prediction": float(prediction)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
