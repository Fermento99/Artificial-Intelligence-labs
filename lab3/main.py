# Paweł Kajanek

import sys
from mnist import *
from utils import *


def getCentroids(k):
    return randomCentroids(k)

def saveInertion(inertion, k):
    inertionPath = './k{}/inertion.txt'.format(k)
    makeDirs(inertionPath)
    inertionFile = open(inertionPath, 'w')
    inertionFile.write('\n'.join([str(i) for i in inertion]))
    inertionFile.close()

def iteration(centroids, points):
    clusters = [[] for _ in range(len(centroids))]

    for i in range(len(centroids)):
        clusters[i] = []

    for point in points:
        dists = [dist(point, centroid) for centroid in centroids]
        clusters[dists.index(min(dists))].append(point)
    
    inertion = 0
    for clusterId, cluster in enumerate(clusters):
        centroid = center(cluster)
        centroids[clusterId] = centroid
        for point in cluster:
            inertion += dist(centroid, point) ** 2

    return centroids, inertion


def showResult(centroids, points, labels, path):
    clusters = {}
    elements = []

    for i in range(len(centroids)):
        clusters[i] = []

    for i in range(len(points)):
        dists = [dist(points[i], centroid) for centroid in centroids]
        clusters[dists.index(min(dists))].append(labels[i])
    
    for cluster in clusters.values():
        element = [0 for _ in range(10)]
        for label in cluster:
            element[label] += 1
        elements.append(element)
    printResult(centroids, elements, labelSize(labels), path)


def main(clusterCount):
    points, labels = getMnist()
    centroids = getCentroids(clusterCount)
    inertionList = []
    
    showResult(centroids, points, labels, 'k{}/starting'.format(clusterCount))
    
    for _ in range(2):
        centroids, inertion = iteration(centroids, points)
        inertionList.append(inertion)
        print("inertion: ", inertion)
    
    while abs(inertionList[-2] - inertionList[-1]) > 500:
        centroids, inertion = iteration(centroids, points)
        inertionList.append(inertion)
        print("inertion: ", inertion)
    
    myPoints, myLabels = tests('./digits')
    showResult(centroids, myPoints, myLabels, 'k{}/finished'.format(clusterCount))
    
    saveInertion(inertionList, clusterCount)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(10)