import logging
from flask import Flask, request, jsonify
import os
import opslib

# Set path for the model
cwd = os.path.abspath(os.path.dirname(__file__))
given_path = "model"
model_path = os.path.abspath(os.path.join(cwd, given_path))

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    app.logger.info(f"Inside / endpoint for health check")
    return '', 200

# Not getting used
@app.route("/health", methods=['GET'])
def health_check():
    app.logger.info(f"DEBUG ASHOK SHLOK /health ENDPOINT")
    return '', 200

@app.route("/predict", methods=['POST'])
def predict():
    """
    This endpoint is used to make predictions based on the input data.

    It accepts a POST request with a JSON payload. The JSON payload should contain a key 'instances'
    with a value of a two-dimensional array of numbers. Each sub-array represents a single instance
    for which a prediction is to be made.

    The endpoint returns a JSON response with a key 'predictions'. The value is an array of predictions
    corresponding to the input instances.

    If an error occurs during the prediction process, the endpoint returns a JSON response with a key 'key'
    and a value 'exception', along with another key 'value' containing the exception message.

    :return: A JSON response containing the predictions or an error message.
    """

    app.logger.info(f"inside /predict endpoint")

    try:
        json_payload = request.json
        app.logger.info(f"input json payload == {json_payload} ")
        instances = json_payload.get('instances', [])
        predictions = opslib.predict(instances)
        app.logger.info(f"predictions: {predictions}")

        ### Vertex AI reponse format ###
        return jsonify({"predictions": predictions})
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return {"key": "exception", "value": str(e)} # not a good practice to return exception message. just for testing

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
