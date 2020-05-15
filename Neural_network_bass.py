import tensorflow
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Activation
from keras.layers import LSTM
import bass_data as data
from keras import optimizers
import os
import msgpack
import numpy as np
import guitarpro


class NeuralNetwork:
    def __init__(self, path):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        self.model = Sequential()
        self.model.add(LSTM(50, input_shape=(data.maxBeats, 6), return_sequences=True, activation='sigmoid'))
        self.model.add(Dense(6, activation='sigmoid'))
        self.model.compile(loss='mean_absolute_error', optimizer='RMSprop', metrics=['accuracy'])
        self.model.load_weights(path)

    def Predict(self, x, path):
        x_test, fs, key, mm = data.returnTestData(x, path)

        predict = self.model.predict(x_test)
        return predict, fs, key, mm
