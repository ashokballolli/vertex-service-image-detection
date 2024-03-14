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
        logging.info(f"input json payload == {json_payload} ")
        instances = json_payload.get('instances', [])
        image_data = (instances[0]).get('ser-image', [])
        predictions = opslib.predict(image_data)
        res = {
            "model": "MNIST",
            "number": int(predictions[0]),
            "version": {
                "version_name": "agb-v1",
                "model_id": "test_model_id_123",
            }
        }
        logging.info(f"predictions: {res}")
        return res
    except Exception as e:
        logging.info(f"Exception: {str(e)}")
        return {"key": "exception", "value": str(e)}
