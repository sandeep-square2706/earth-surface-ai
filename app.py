from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔴 Replace this later with your REAL Azure ML endpoint
AZURE_ML_ENDPOINT = "PASTE_YOUR_ENDPOINT_URL_HERE"
API_KEY = "PASTE_YOUR_API_KEY_HERE"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    image_bytes = file.read()

    headers = {
        "Content-Type": "application/octet-stream",
        "Authorization": f"Bearer {API_KEY}"
    }

    # 🔹 Dummy response (works now)
    result = {
        "prediction": "Forest",
        "confidence": "82%"
    }

    # 🔹 Uncomment when Azure ML endpoint is ready
    # response = requests.post(AZURE_ML_ENDPOINT, data=image_bytes, headers=headers)
    # result = response.json()

    return render_template("index.html",
                           prediction=result["prediction"],
                           confidence=result["confidence"])

if __name__ == "__main__":
    app.run(debug=True)
