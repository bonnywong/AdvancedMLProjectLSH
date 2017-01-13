# OBS! Allt i denna fil är änsålänge specifikt för dataset1.
from datakeeper_dataset1 import Datakeeper,saveData,loadData
import numpy as np


def getQueryPoints():
    # fixa denna
    # två första punkterna från dataset1 bara:
    array = [np.array([0.002188,0.000000,0.000000,0.620521,0.010313,0.007083,0.043021,0.310729,0.000729,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000,0.000729,0.000000,0.000000,0.000000,0.002917,0.000000,0.000000,0.000000,0.000937,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000]),np.array([0.002917,0.315417,0.188854,0.004440,0.000001,0.000001,0.000004,0.000032,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000208,0.001563,0.003750,0.002708,0.007917,0.326562,0.133958,0.011771])]
    return array

def main():
    # läs in data som är sparat
    data1 = loadData(filename="temp1")

    # analysera:
    numberOfNeighbors = 5
    queryPoints = getQueryPoints()
    nearestNeighbors = []

    for point in queryPoints:
        nearestNeighbors.append(data1.getNN(point,numberOfNeighbors))

    print(nearestNeighbors)


if __name__ == '__main__':
    main()