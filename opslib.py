# import joblib
# import os
# import numpy as np
# import pandas as pd
# import logging
# import json
# import tensorflow as tf
#
# logging.basicConfig(level=logging.INFO)
# cwd = os.path.abspath(os.path.dirname(__file__))
#
# cwd = os.path.abspath(os.path.dirname(__file__))
#
# # Define the possible classes (numbers 0 to 9)
# number_class = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#
# def get_num_class(probability_result):
#     """Returns the class with the highest probability."""
#     # Use argmax to find the index of the maximum probability
#     return number_class[tf.argmax(probability_result[0])]
#
# def resizing_img(img):
#     """Preprocesses and resizes the input image for model prediction."""
#     img = tf.image.decode_jpeg(img)
#     img = tf.image.resize(img, [28, 28])
#     img = tf.squeeze(img, axis=-1)
#     img = img / 255.0
#     img = tf.expand_dims(img, axis=0)
#     return img
#
#
# def get_transformed_ip_data_for_model(IMG_FILE):
#
#     img_path = os.path.join(cwd, "test_images", IMG_FILE)
#     img = tf.io.read_file(img_path)
#
#     # Preprocess and resize the image
#     img = resizing_img(img)
#
#     # Convert to list for Vertex AI endpoint prediction
#     return img.numpy().tolist()
#
#
# def load_model():
#     """
#     Load the pre-trained machine learning model
#     Returns:
#         model: The loaded machine learning model
#     """
#     given_path = "model"
#     model_path = os.path.abspath(os.path.join(cwd, given_path))
#
#     # ASHOK
#     model_path = os.path.abspath(os.path.join(cwd, "MNIST_model"))
#     # model = joblib.load(os.path.abspath(
#     #     os.path.join(model_path,
#     #                  'housing_price_model.joblib')))
#     return tf.keras.models.load_model(model_path)
#
#
# def formatting(prediction):
#     """Round the prediction to the nearest integer."""
#     return np.around(prediction, 0)
#
#
# def predict(instances):
#     """Make predictions for a list of instances"""
#     #  Assume only one element in instances ex: request for 1 image prediction
#
#     model = load_model()
#     # predictions = []
#     # for instance in instances:
#     #     df = pd.DataFrame.from_dict([json.loads(instance)])
#     #     prediction = model.predict(df)
#     #     prediction = formatting(prediction)
#     #     predictions.append(prediction[0])
#
#     # return model.predict(instances)
#     print("ASHOK instances ==> ", instances)
#     print("ASHOK instances ==> ", type(instances)) # <class 'list'>
#     pred = model.predict(instances)
#
#     return {"number": get_num_class(pred)}
#
#
# def predict_local(instances):
#     pass