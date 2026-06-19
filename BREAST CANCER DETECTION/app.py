from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model & Scaler
model = pickle.load(open("breast_cancer_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['area_mean']),
            float(request.form['concavity_mean']),
            float(request.form['concave_points_mean']),
            float(request.form['radius_worst']),
            float(request.form['perimeter_worst']),
            float(request.form['area_worst']),
            float(request.form['concave_points_worst'])
        ]

        data = np.array(features).reshape(1, -1)
        data = scaler.transform(data)

        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)

        if prediction == 0:
            result = "⚠️ Malignant (Cancer Detected)"
            confidence = round(probability[0][0] * 100, 2)
        else:
            result = "✅ Benign (No Cancer Detected)"
            confidence = round(probability[0][1] * 100, 2)

        return render_template(
            'index.html',
            prediction_text=result,
            confidence=confidence
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {e}",
            confidence=""
        )

if __name__ == "__main__":
    app.run(debug=True)