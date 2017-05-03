from keras.datasets import mnist
import matplotlib.pyplot as plt
import random
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils

# import (download) data from MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

plt.figure()

plt.subplot(131)
plt.imshow(X_train[random.randrange(len(X_train))], cmap=plt.get_cmap('gray'))
plt.subplot(132)
plt.imshow(X_train[random.randrange(len(X_train))], cmap=plt.get_cmap('gray'))
plt.subplot(133)
plt.imshow(X_train[random.randrange(len(X_train))], cmap=plt.get_cmap('gray'))

# show the plot
plt.suptitle('Training data examples')
plt.show()

seed = 1
pixel_max_val = 255
numpy.random.seed(seed)

num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32') / pixel_max_val
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32') / pixel_max_val

# convert e.g. 5 to 0000100000
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]


# build simple NN model
def baseline_nn_model():
    model = Sequential()
    # input layer
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    # output layer
    # a softmax activation function is used on the output layer to turn the outputs into probability-like values and
    # allow one class of the 10 to be selected as the model’s output prediction
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    # logarithmic loss is used as the loss function (called categorical_crossentropy in Keras) and the efficient
    # ADAM gradient descent algorithm is used to learn the weights.
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

#model = baseline_nn_model()
#model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)

#scores = model.evaluate(X_test, y_test, verbose=0)
#print('Baseline Error: %.2f%%' % (100 - scores[1]*100))


