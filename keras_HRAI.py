import keras
from keras.preprocessing import image
import keras.utils as image
import numpy as np
import sys

# Load the trained model
model = keras.models.load_model('model.h5')

# Take the image path from the command line argument
img_path = sys.argv[1]

# Load and preprocess the image
img = image.load_img(img_path, target_size = (460, 570))
img = image.img_to_array(img)
img = img/255.
img = np.expand_dims(img, axis=0)

# Make a prediction
pred = model.predict(img)

# Print the predicted rating
print("Predicted rating: ", pred[0][0])