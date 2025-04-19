from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/trained_model.pkl")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        if request.method == "POST":
            data = request.get_json()
            W = float(data["W"])
            X = float(data["X"])
        else:
            W = float(request.args.get("W"))
            X = float(request.args.get("X"))
        input_data = np.array([[W, X]])
        y_pred = model.predict(input_data)[0]
        return jsonify({"predicted_engagement_score": round(y_pred, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
