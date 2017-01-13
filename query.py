# OBS! Allt i denna fil är änsålänge specifikt för dataset1.
from datakeeper_dataset1 import Datakeeper,saveData,loadData
from parse import parse_dataset
import numpy as np
import pandas


def getQueryPoints(multiplier,translation):
    # fixa denna, i framtiden ska den läsa in från fil genom parse_dataset
    queryPoints_filename = "Dataset_1_query.rcd"
    queryPoints,queryPoints_dimension = parse_dataset(queryPoints_filename,multiplier,translation)
    

    # om man vill läsa in de två första punkterna från dataset1 bara:
    # array = [np.array([0.002188,0.000000,0.000000,0.620521,0.010313,0.007083,0.043021,0.310729,0.000729,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000,0.000729,0.000000,0.000000,0.000000,0.002917,0.000000,0.000000,0.000000,0.000937,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000]),np.array([0.002917,0.315417,0.188854,0.004440,0.000001,0.000001,0.000004,0.000032,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000208,0.001563,0.003750,0.002708,0.007917,0.326562,0.133958,0.011771])]
    return queryPoints
    
def getDlsh(point,neighbor,multiplier):
    #print(point)

    
    distance = np.linalg.norm(point-np.array(neighbor))/multiplier
    
    return distance

def main():
    # läs in data som är sparat från preprocessing
    data1 = loadData(filename="temp1")
    # läs in sr-Tree data 
    srDistances = np.genfromtxt('distance.csv', delimiter=',')
    # analysera:
    numberOfNeighbors = 5
    queryPoints = getQueryPoints(data1.multiplier,data1.translation)
    
    nearestNeighbors = []
    distances = []

    i =0 
    # acc - Accurcy, E - Effictive error
    acc = 0
    E = 0
    Q = len(queryPoints)
    for point in queryPoints:
        
        NN = data1.getNN(point,numberOfNeighbors)
        nearestNeighbors.append(NN)
        
        #avstånd d till närmsta granne
        d=getDlsh(point,NN[0],data1.multiplier)
        
        distances.append(d)
        E += d/srDistances[i]
        if abs(srDistances[i]-d)<1e-4:
            acc+=1
        i+=1
           
    print(acc/Q)
    print(E/Q)
        
    #print(nearestNeighbors)
    #print(queryPoints[198])

if __name__ == '__main__':
    main()