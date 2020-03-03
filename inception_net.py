from keras.applications import InceptionV3
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import argparse
import cv2

MODELS = {
	"inception": InceptionV3,
}

inputShape = (200, 200)
preprocess = preprocess_input

Network = MODELS["inception"]
model = Network(weights="imagenet")

image = load_img("img_name.jpg", target_size=inputShape)
image = img_to_array(image)
# our input image is now represented as a NumPy array of shape

image = np.expand_dims(image, axis=0)

image = preprocess(image)
preds = model.predict(image)
P = imagenet_utils.decode_predictions(preds)

# loop over the predictions and display the rank-5 predictions +
# probabilities to our terminal
for (i, (imagenetID, label, prob)) in enumerate(P[0]):
	print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
