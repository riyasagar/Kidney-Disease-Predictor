# Flask app for Kidney Disease Prediction

from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# ------------------------
# Load the trained model
# ------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'Kidney_Disease_Prediction_Model.pkl')
loaded_model = None

try:
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 0:
        loaded_model = joblib.load(MODEL_PATH)
        print("Machine learning model loaded successfully.")
    else:
        print(f"Error: Model file '{MODEL_PATH}' not found or empty. Make sure you pushed it to GitHub.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")

# ------------------------
# Flask Routes
# ------------------------
@app.route('/')
def home():
    """Render the main HTML page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict CKD from input data"""
    if loaded_model is None:
        return jsonify({'error': 'Model not available. Please check the server logs.'}), 500

    try:
        data = request.get_json(force=True)

        # Build input feature dictionary
        input_features = {
            'age': data.get('age', 0),
            'bp': data.get('bp', 0),
            'sg': data.get('sg', 0),
            'al': data.get('al', 0),
            'su': data.get('su', 0),
            'rbc': 0,
            'pc': 0,
            'pcc': 0,
            'ba': 0,
            'bgr': data.get('bgr', 0),
            'bu': 0,
            'sc': data.get('sc', 0),
            'sod': 0,
            'pot': 0,
            'hemo': data.get('hemo', 0),
            'pcv': 0,
            'wc': 0,
            'rc': 0,
            'htn': 0,
            'dm': 0,
            'cad': 0,
            'appet': 0,
            'pe': 0,
            'ane': 0
        }

        input_data = pd.DataFrame([list(input_features.values())], columns=list(input_features.keys()))

        # Prediction
        prediction = loaded_model.predict(input_data)
        probability = loaded_model.predict_proba(input_data)[0][1]

        result = 'Kidney Disease (CKD)' if prediction[0] == 1 else 'No Kidney Disease (Not CKD)'
        probability_percent = f'{probability * 100:.2f}%'

        return jsonify({'prediction': result, 'probability': probability_percent})

    except KeyError as e:
        return jsonify({'error': f'Missing data field: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # For local testing
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
