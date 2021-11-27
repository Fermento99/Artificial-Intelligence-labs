# Paweł Kajanek

import numpy as np
import os
from matplotlib import pyplot as plt

size = 28

def dist(a, b):
    return np.linalg.norm(a-b)

def center(points):
    if len(points) > 0:
        return sum(points)/len(points)
    return np.zeros((size, size), np.float64)

def randomCentroids(k):
    centroids = [np.zeros((size, size), np.float32) for _ in range(k)]
    for i in range(len(centroids)):
        probability = 0
        rand = 1
        if i == 0:
            centroids[i] = np.random.uniform(0, 1, (28, 28))
            continue
    
        while rand > probability:
            centroid = np.random.uniform(0, 1, (28, 28))
            dists = []
            for existing in centroids[0:i]:
                dists.append(dist(centroid, existing))
            
            probability = min(dists)**2 / sum([d**2 for d in dists])
            rand = np.random.uniform(0, 1)
        centroids[i] = centroid
    
    return centroids

def makeDirs(path):
    dirs = '/'.join(path.split('/')[0:-1])
    if not os.path.exists(dirs):
        os.makedirs(dirs)

def saveFile(path):
    makeDirs(path)
    plt.savefig(path)
    plt.close()

def printTable(elements, maxes): 
    counts = 0
    print("┌--------------┬----------┬----------┬----------┬----------┬----------┬----------┬----------┬----------┬----------┬----------┬----------┐")
    print("|  ####### &&  |   size   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |  {:5d}   |".format(*range(10)))
    print("├--------------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┤")
    for index, element in enumerate(elements):
        count = sum(element)
        counts += count
        element = [(element[i]/maxes[i])*100 for i in range(len(element))]
        elements[index] = element
        print("|  cluster {:2d}  |  {:6d}  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |".format(index, count, *element))
    
    print("├--------------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┼----------┤")
    print("|  sum         |  {:6d}  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |  {:5.1f}%  |".format(counts, *np.sum(elements, 0)))
    print("└--------------┴----------┴----------┴----------┴----------┴----------┴----------┴----------┴----------┴----------┴----------┴----------┘")


def printResult(centroids, elements, maxes, path):
    printTable(elements, maxes)
    
    plt.imshow(elements, interpolation='nearest', cmap='binary')
    saveFile('./{}/alloc_matrix.png'.format(path))

    matrixToImg(centroids)
    saveFile('./{}/centroids.png'.format(path))


def matrixToImg(matrices):
    long = int(np.ceil(np.sqrt(len(matrices))))
    short = int(np.ceil(len(matrices)/long))
    for i, matrix in enumerate(matrices):
        subplot = plt.subplot(short, long, i + 1)
        subplot.imshow(matrix, interpolation='nearest', cmap='binary')
        subplot.title.set_text('centroid {}'.format(i))
        subplot.axis('off')