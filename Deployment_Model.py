from flask import Flask, request, jsonify
import pickle
import numpy as np

# Create a Flask instance
app = Flask(__name__)

# Load the trained model
with open('finalized_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return "California Housing Price Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Expecting JSON in the format:
    {
        "features": [value1, value2, ..., valueN]
    }
    """
    data = request.get_json(force=True)
    # Extract features
    input_features = data['features']  # e.g., [<val1>, <val2>, ...]
    # Convert to array (reshape if necessary)
    input_array = np.array(input_features).reshape(1, -1)
    # Model prediction
    prediction = model.predict(input_array)
    # Return prediction in JSON format
    return jsonify({"predicted_price": float(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
