import pickle
from flask import Flask, request, jsonify

app = Flask('placementstatus')

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

@app.route('/', methods=['GET'])
def home():
    return (
        "API is running. Use the /predict endpoint for predictions. See README file for instructions.",
        200
    )

@app.route('/predict', methods=['POST'])
def predict():
    student = request.get_json()

    X = dv.transform([student])
    y_pred = model.predict_proba(X)[0, 1]
    placementstatus = y_pred >= 0.5

    result = {
        'placementstatus_probability': float(y_pred),
        'placementstatus': bool(placementstatus)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9090)