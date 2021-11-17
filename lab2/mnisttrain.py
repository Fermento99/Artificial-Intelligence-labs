# Paweł Kajanek

import tensorflow as tf
from model import model, loss_fn

def train():
    mnist = tf.keras.datasets.mnist
    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    print()
    print('starting accuracy')
    model.evaluate(x_test,  y_test, verbose=2)
    model.fit(x_train, y_train, epochs=5)
    print()
    print('mnist accuracy')
    model.evaluate(x_test,  y_test, verbose=2)
    
    return model
