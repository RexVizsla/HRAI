import numpy as np
import os
import json
from keras.preprocessing import image
import keras.utils as image
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split

folder_path = r'C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated'

# Load the data
X = []
y = []
for file in os.listdir(folder_path):
    if file.endswith('.jpg'):
        img = image.load_img(os.path.join(folder_path, file), target_size = (460, 570))
        img = image.img_to_array(img)
        X.append(img)
        json_file = file.replace('.jpg', '.json')
        with open(os.path.join(folder_path, json_file)) as f:
            data = json.load(f)
            y.append(data['rating'])

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Format
X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)


# Create the CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=X_train[0].shape))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2)) # Add dropout with a rate of 0.2
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2)) # Add dropout with a rate of 0.2
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2)) # Add dropout with a rate of 0.2
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2)) # Add dropout with a rate of 0.2
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2)) # Add dropout with a rate of 0.2
model.add(Dense(1))


# Compile and train the model
model.compile(optimizer='rmsprop', loss='mean_squared_error')

checkpointer = ModelCheckpoint(filepath='model.h5', verbose=1, save_best_only=True)

model.fit(X_train, y_train, epochs=7, batch_size=16, callbacks=[checkpointer],
          validation_data=(X_test, y_test))
