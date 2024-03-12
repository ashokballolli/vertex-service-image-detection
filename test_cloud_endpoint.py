# from google.cloud import aiplatform
# import json
#
# def prepare_test_data():
#     test_data = {
#         "Street": "Pave",
#         "LotFrontage": 80.0,
#         "OverallQual": 5,
#         "GarageCond": "TA",
#         "1stFlrSF": 896,
#         "TotalBsmtSF": 882.0,
#         "LotArea": 11622,
#         "BsmtFinType2": "LwQ"
#     }
#     return json.dumps(test_data)
#
# def predict_custom_trained_model(instances, project_number, endpoint_id):
#     """
#     Uses Vertex AI endpoint to make predictions
#     Args:
#         instances (str): JSON-encoded instances.
#         project_number (str): Google Cloud project number.
#         endpoint_id (str): Vertex AI endpoint ID.
#     Returns:
#         dict: Prediction results
#     """
#     endpoint = aiplatform.Endpoint(
#         endpoint_name=f"projects/{project_number}/locations/us-central1/endpoints/{endpoint_id}"
#     )
#     result = endpoint.predict(instances=[instances])
#     return result.predictions
#
# if __name__ == "__main__":
#     test_data = prepare_test_data()
#
#     # Make predictions using the custom trained model
#     prediction_result = predict_custom_trained_model(
#         instances=test_data,
#         project_number="65143767267",
#         endpoint_id="1431064961085341696"
#     )
#
#     print(prediction_result)