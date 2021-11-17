# Paweł Kajanek

from mnisttrain import train
import tensorflow as tf
import numpy as np
import os

model = train()

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

myX, myY = tests('./digits')
donX, donY = tests('./digits-donald', True)

print()
print('My accuracy')
model.evaluate(myX,  myY, verbose=2)

print()
print('Donald accuracy')
model.evaluate(donX,  donY, verbose=2)