from flask import Flask, jsonify, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    raise RuntimeError("Model file not found. Please ensure 'model.pkl' exists.")
except pickle.UnpicklingError:
    raise RuntimeError("Error loading the model. The file may be corrupted.")

@app.route('/health', methods=['GET'])
def api_health():
    return jsonify({"message": "API is up and running"}), 200

@app.route('/predict', methods=['POST'])
def predict_api():
    try:
        # Check if the request has JSON content
        if not request.is_json:
            return jsonify({'error': 'Request must be in JSON format'}), 400
        
        data = request.get_json()

        # Validate 'features' in JSON data
        if 'features' not in data:
            return jsonify({'error': "'features' key is missing in the request"}), 400
        
        features = data['features']

        # Validate features data
        if not isinstance(features, list) or not all(isinstance(x, (int, float)) for x in features):
            return jsonify({'error': "'features' must be a list of numbers"}), 400
        
        features = np.array([features])
        
        # Predict and return the result
        prediction = model.predict(features)
        return jsonify({'prediction': prediction[0]})
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except TypeError as te:
        return jsonify({'error': str(te)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    return jsonify({
        "Train Data Accuracy": "97.42%",
        "Test Data Accuracy": "81.77%",
        "Mean Squared Error (MSE)": "2464996572.5548997",
        "R2 Score": "81.77%",
        "Model Information": "A Forest Regressor, often implemented as a Random Forest Regression, is an ensemble learning method that combines multiple decision trees. Each tree is trained on a random subset of data, and the final prediction is the average of the predictions from all trees."
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
