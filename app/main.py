import json

from fastapi import FastAPI
import app.opslib as opslib
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Inside / endpoint for health check"}

@app.get("/health")
def health_check():
    return {"message": "DEBUG ASHOK SHLOK /health ENDPOINT"}

@app.post("/custom-predict")
def predict(json_payload: dict):
    try:
        logging.info("Inside /predict endpoint")
        logging.info(f"input json payload == {json_payload}, type == {type(json_payload)}")

        if not isinstance(json_payload, dict):
            json_payload = json.loads(json_payload)

        instances = json_payload.get('instances', [])
        logging.info(f"input instances == {instances}, type == {type(instances)}")
        if not isinstance(instances, list):
            instances = [instances]

        image_data = (instances[0]).get('ser-image', [])
        logging.info(f"input image_data == {image_data}, type == {type(image_data)}")
        predictions = opslib.predict(image_data)
        logging.info(f"predictions output == {predictions}, type == {type(predictions)}")
        res = {
            "model": "MNIST",
            "number": predictions,
            "version": {
                "version_name": "agb-v1",
                "model_id": "test_model_id_123",
            }
        }
        logging.info(f"result: {res}")
        return {"predictions": [res]}
    except Exception as e:
        logging.info(f"Exception: {str(e)}")
        return {"key": "exception", "value": str(e)}
