# OBS! Allt i denna fil är änsålänge specifikt för dataset1.
from datakeeper_dataset1 import Datakeeper,saveData,loadData
from parse import parse_dataset
import numpy as np
import pylab as pb

def getQueryPoints(multiplier,translation):
    queryPoints_filename = "Dataset_1_query.rcd"
    queryPoints,queryPoints_dimension = parse_dataset(queryPoints_filename,multiplier,translation)

    # om man vill läsa in de två första punkterna från dataset1 bara:
    # array = [np.array([0.002188,0.000000,0.000000,0.620521,0.010313,0.007083,0.043021,0.310729,0.000729,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000,0.000729,0.000000,0.000000,0.000000,0.002917,0.000000,0.000000,0.000000,0.000937,0.000000,0.000000,0.000000,0.000417,0.000000,0.000000,0.000000]),np.array([0.002917,0.315417,0.188854,0.004440,0.000001,0.000001,0.000004,0.000032,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000208,0.001563,0.003750,0.002708,0.007917,0.326562,0.133958,0.011771])]
    return queryPoints
    
def getDlsh(point,neighbor,multiplier):
    #print(point)
    distance = np.linalg.norm(point-np.array(neighbor))/multiplier
    return distance

def getPointDist(points,multiplier):
    N=len(points)
    PointSetDistances=[]
    
    for i in range (0,N):
        for j in range(i+1,N):
            
            d = abs(getDlsh(points[i],points[j],multiplier))
            PointSetDistances.append(d*multiplier)
            
    M = len(PointSetDistances)
    print("bla: "+ str(M))
    pb.hist(PointSetDistances,M/100)

            

    
def main():
    # läs in data som är sparat från preprocessing
    data1 = loadData(filename="temp1")
    # läs in sr-Tree data 
    srDistances = np.genfromtxt('distance.csv', delimiter=',')
    srDistancesVector = np.genfromtxt('Dataset_1_distanceVector.csv', delimiter=',')
    srDistancesVector = np.reshape(srDistancesVector,(1000,10)) # every row contains the 10 NN for a point
    # analysera:

    numberOfNeighbors = 10

    queryPoints = getQueryPoints(data1.multiplier,data1.translation)
    
    multiplier = data1.multiplier
    nearestNeighbors = []

    distances = [] # avstånd till närmsta granne
    # distanceVectors = [] # avstånd till alla grannar

    E = 0 # add to this below
    Q = len(queryPoints)
    # totalNumberOfMissedNeighbors = 0
    numberOfQueriesWithMisses = Q # subtract from this below
    for i,point in enumerate(queryPoints):
        NN = data1.getNN(point,numberOfNeighbors)
        nearestNeighbors.append(NN)

        numberOfMissedNeighbors=(numberOfNeighbors-len(NN))
        if numberOfMissedNeighbors==0:
            # distanceVectors.append([getDlsh(point,neighbor,data1.multiplier) for neighbor in NN]) # avstaand till alla grannar
            for neighborNumber,neighbor in enumerate(NN):
                E += getDlsh(point,neighbor,data1.multiplier)/srDistancesVector[i,neighborNumber]
            numberOfQueriesWithMisses-=1
        # else:
        #     distanceVectors.append(0)
        #     totalNumberOfMissedNeighbors+=numberOfMissedNeighbors
        if(i%100 == 0):
            print("[query] Query point: " + str(i))
    missRatio = numberOfQueriesWithMisses/Q
    E=E/(Q*numberOfNeighbors)
    print("Error: ",E)
    print("Miss ratio: ",missRatio)
    #getPointDist(queryPoints[0:int(0.2*len(queryPoints))],multiplier

    #print(nearestNeighbors)
    

if __name__ == '__main__':
    main()