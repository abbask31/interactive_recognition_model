import tensorflow as tf
import pandas as pd
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, AveragePooling2D
# import matplotlib.pyplot as plt

(train_x, train_y), (test_x, test_y) = mnist.load_data()
train_x.shape, train_y.shape, test_x.shape, test_y.shape

# normalize data
train_x = train_x.astype(np.float32)/255
test_x = test_x.astype(np.float32)/255

train_x = np.expand_dims(train_x, -1)
test_x = np.expand_dims(test_x, -1)

#one hot encoding the data 
train_y = tf.keras.utils.to_categorical(train_y)
test_y = tf.keras.utils.to_categorical(test_y)

train_y

# create model 
model = Sequential()
# model.add(Conv2D(32, (3,3), input_shape = (28,28,1), activation = 'relu'))
# # model.add(MaxPool2D((2,2)))
# model.add(AveragePooling2D(pool_size=(2,2))) 
# model.add(Conv2D(64, (3,3), activation = 'relu'))
# # model.add(MaxPool2D((2,2)))
# model.add(AveragePooling2D(pool_size=(2,2))) 
# model.add(Flatten())
# model.add(Dropout(0.2))
# model.add(Dense(10, activation = "softmax"))

model.add(Dense(512, input_dim=784, activation = "relu"))
# An "activation" is just a non-linear function applied to the output
# of the layer above. Here, with a "rectified linear unit",
# we clamp all values below 0 to 0.

# Dropout helps protect the model from memorizing or "overfitting" the training data
model.add(Dropout(0.2))

model.add(Dense(512), activation = 'relu')

model.add(Dropout(0.2))

model.add(Dense(512), activation = 'relu')

model.add(Dropout(0.2))

model.add(Dense(10), activation = 'softmax')
# This special "softmax" activation among other things,
# ensures the output is a valid probaility distribution, that is
# that its values are all non-negative and sum to 1.


# observe and compile model
model.summary()
model.compile(loss = tf.keras.losses.categorical_crossentropy, optimizer = 'adam', metrics=['accuracy'])
model.fit(train_x, train_y, batch_size = 16, epochs=5, validation_split = 0.3, )

# evaluate the accuracy
model.evaluate(test_x, test_y, batch_size=128)

# save model in .h5
model.save("mnist_model_new.h5")