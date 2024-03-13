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
    app.logger.info(f"DEBUG ASHOK SHLOK / ENDPOINT")
    # html = "<h3>Model Serving</h3>"
    # return html.format(format)
    return '', 200

@app.route("/health", methods=['GET'])
def health_check():
    app.logger.info(f"DEBUG ASHOK SHLOK /health ENDPOINT")
    return '', 200

@app.route("/predict", methods=['POST'])
def predict():
    app.logger.info(f"DEBUG ASHOK SHLOK /predict ENDPOINT")

    try:
        json_payload = request.json
        app.logger.info(f"DEBUG json_payload == {json_payload} ")
        instances = json_payload.get('instances', [])
        app.logger.info(f"DEBUG instances: {instances}")

        predictions = opslib.predict(instances)
        app.logger.info(f"DEBUG predictions: {predictions}")

        ### Vertex AI reponse format ###
        return jsonify({"predictions": predictions})
    except Exception as e:
        app.logger.error(f"DEBUG Error: {str(e)}")
        return {"key": "exception", "value": str(e)}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
