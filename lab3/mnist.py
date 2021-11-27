# Paweł Kajanek

import tensorflow as tf
import os
import numpy as np


def getMnist():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    return x_train/255, y_train

def labelSize(labels):
    element = [0 for _ in range(10)]
    for label in labels:
        element[label] += 1
    return element

def tests(path, invert=False):
    myTestX = []
    myTestY = []
    for file in os.listdir(path):
        filepath = path + '/' + file
        myTestX.append(tf.image.decode_png(tf.io.read_file(filepath), 1))
        myTestY.append(int(file.split('_')[0]))

    myTestX = (np.array(myTestX) / -255.0) + 1.0 if invert else np.array(myTestX) / 255.0
    myTestY = np.array(myTestY)

    return myTestX, myTestY
