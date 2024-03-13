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
    html = "<h3>Model Serving</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    json_payload = request.json
    instances = json_payload.get('instances', [])
    app.logger.info(f"json_payload: {instances}")

    predictions = opslib.predict(instances)
    app.logger.info(f"predictions: {predictions}")

    ### Vertex AI reponse format ###
    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
