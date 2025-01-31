import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model and scaler
with open('important_features_model.pkl', 'rb') as f_in:
    model, scaler = pickle.load(f_in)

# Initialize Flask app
app = Flask('placement_prediction')

# Function to preprocess student data
def preprocess_student(student):
    """Convert categorical values and ensure data format is correct."""
    student['placementtraining'] = 1 if student['placementtraining'].lower() == 'yes' else 0
    student['extracurricularactivities'] = 1 if student['extracurricularactivities'].lower() == 'yes' else 0
    return student

# Define the prediction function
def predict_single(student, model, scaler):
    student = preprocess_student(student)  # Convert categorical values
    student_df = pd.DataFrame([student])  # Convert dict to DataFrame
    student_transformed = scaler.transform(student_df)  # Apply scaler
    y_pred = model.predict_proba(student_transformed)[:, 1]
    return y_pred[0]

@app.route('/predict', methods=['POST'])
def predict():
    student = request.get_json()
    prediction = predict_single(student, model, scaler)
    placed = prediction >= 0.5

    result = {
        'placement_probability': float(prediction),
        'placed': bool(placed),
    }

    return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2525)
