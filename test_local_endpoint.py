import json


def prepare_test_data():
    test_data = {
        "Street": "Pave",
        "LotFrontage": 80.0,
        "OverallQual": 5,
        "GarageCond": "TA",
        "1stFlrSF": 896,
        "TotalBsmtSF": 882.0,
        "LotArea": 11622,
        "BsmtFinType2": "LwQ"
    }
    return json.dumps(test_data)


def predict_custom_trained_model(instances, project_number, endpoint_id):
    """
    Uses Vertex AI endpoint to make predictions
    Args:
        instances (str): JSON-encoded instances.
        project_number (str): Google Cloud project number.
        endpoint_id (str): Vertex AI endpoint ID.
    Returns:
        dict: Prediction results
    """
    # endpoint = aiplatform.Endpoint(
    #     endpoint_name=f"projects/{project_number}/locations/us-central1/endpoints/{endpoint_id}"
    # )
    # result = endpoint.predict(instances=[instances])
    # return result.predictions


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

''' 
import requests

# Define the URL of the endpoint
url = 'http://127.0.0.1:8080/'

# Make the GET request
response = requests.get(url)

# Check the response
if response.status_code == 200:
    print('GET request successful!')
    print('Response:', response.text)
else:
    print('GET request failed. Status code:', response.status_code)
'''


import requests

# Define the URL of the endpoint
url = 'http://127.0.0.1:8080/predict'


# Define the data you want to send in the POST request
def prepare_test_data():
    test_data = {
        "Street": "Pave",
        "LotFrontage": 80.0,
        "OverallQual": 5,
        "GarageCond": "TA",
        "1stFlrSF": 896,
        "TotalBsmtSF": 882.0,
        "LotArea": 11622,
        "BsmtFinType2": "LwQ"
    }

    test_data = {
        'MedInc': [3.0],  # Example numerical features, use appropriate values from the dataset
        'HouseAge': [20.0],
        'AveRooms': [5.0],
        'AveBedrms': [2.0],
        'Population': [1000.0],
        'AveOccup': [3.0],
        'Latitude': [37.5],
        'Longitude': [-122.5],
        'Description': ["Charming cottage with a garden"]  # Example text feature
    }

    test_data = {
        'CRIM': 0.18159,
        'ZN': 0.0,
        'INDUS': 7.38,
        'CHAS': 0,
        'NOX': 0.493,
        'RM': 6.376,
        'AGE': 54.3,
        'DIS': 4.5404,
        'RAD': 5,
        'TAX': 287,
        'PTRATIO': 19.6,
        'B': 396.90,
        'LSTAT': 6.87,
        # 'MEDV': 23.1,
        # 'TAXRM': 45.012547
    }

    # CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT

    # CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	                     MEDV	TAXRM
    # 0.18159	0.0	7.38	0	0.493	6.376	54.3	4.5404	5	287	19.6	396.90	6.87	23.1	45.012547
    return json.dumps(test_data)


test_data = prepare_test_data()

data = {
    'instances': test_data
}

# Make the POST request
headers = {'Content-Type': 'application/json'}  # Replace with the appropriate content type
response = requests.post(url, data=json.dumps(data), headers=headers)


# Check the response
if response.status_code == 200:
    print('POST request successful!')
    print('Response:', response.text)
else:
    print('POST request failed. Status code:', response.status_code)
