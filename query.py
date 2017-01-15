
from datakeeper_dataset1 import Datakeeper,saveData,loadData
from parse import parse_dataset
import numpy as np
import pylab as pb
import matplotlib.pyplot as plt

def getQueryPoints(multiplier,translation):
    queryPoints_filename = "d1/Dataset_1_Homemade_query.rcd"
    queryPoints,queryPoints_dimension = parse_dataset(queryPoints_filename,multiplier,translation)

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

def linearSearch():
    srDistancesVector = np.genfromtxt('d2/distanceVector_19000_10.csv', delimiter=',')
    srDistancesVector = np.reshape(srDistancesVector,(1000,10)) # every row contains the 10 NN for a point
    data2 = loadData(filename="temp1")
    queryPoints = getQueryPoints(data2.multiplier,data2.translation)
    antalPoints = 19000

    numberOfNeighbors = 10

    multiplier = data2.multiplier
    nearestNeighbors = []

    distances = [] 

    E = 0 # add to this below
    queryPoints=queryPoints[:100]
    Q = len(queryPoints)
    numberOfQueriesWithMisses = Q # subtract from this below
    for i,queryPoint in enumerate(queryPoints):
        distance = np.empty(antalPoints)
        for j in range(antalPoints):
            distance[j] = getDlsh(queryPoint,data2.getPoint(j),multiplier)
        ind = np.argpartition(distance, numberOfNeighbors)[:numberOfNeighbors]
        NNLinear = sorted(distance[ind])
        nearestNeighbors.append(NNLinear)

        for idx,dist in enumerate(NNLinear):
            E += dist/srDistancesVector[i,idx]
        numberOfQueriesWithMisses-=1
        if(i%5 == 0):
            print("[query] Query point: " + str(i))
    missRatio = numberOfQueriesWithMisses/Q
    E=E/((Q-numberOfQueriesWithMisses)*numberOfNeighbors)
    print("Error: ",E)
    print("Miss ratio: ",missRatio)
    print("We expect an error very close to 1 and a miss ratio of 0.")


def findNNLinearSearch(dataset,point,k,multiplier):
    distance = np.zeros(len(dataset))
    for j in range(len(dataset)):
        distance[j] = getDlsh(point,dataset[j],multiplier)
    ind = np.argpartition(distance, k)[:k]
    NNLinear = sorted(distance[ind])
    return NNLinear

def main():

    data1 = loadData(filename="temp1")

    #srDistances = np.genfromtxt('distance.csv', delimiter=',')
    srDistancesVector = np.genfromtxt('d1/distanceVector_Homemade_10.csv', delimiter=',')
    srDistancesVector = np.reshape(srDistancesVector,(1000,10)) # every row contains the 10 NN for a point
    # analysera:

    numberOfNeighbors = 10

    multiplier = data1.multiplier
    tr = data1.translation
    queryPoints = getQueryPoints(multiplier,tr)

    #Random query points
 #   for i in range(len(queryPoints)):
#        for j in range(len(queryPoints[i])):
#            queryPoints[i][j] = np.random.randint(255, size = 1)


    nearestNeighbors = []
    distancesMeasured = []
    

#    lnDistancesVector = np.zeros((500,10))
 #   for i in range(len(queryPoints)):
  #      lnDistancesVector[i,:] = findNNLinearSearch(data1.dataset1,queryPoints[i],10,multiplier)

    E = 0 # add to this below
    Q = len(queryPoints)
    # totalNumberOfMissedNeighbors = 0
    numberOfQueriesWithMisses = Q # subtract from this below
    for i,point in enumerate(queryPoints):
        NN = data1.getNN(point,numberOfNeighbors)
        nearestNeighbors.append(NN)

        #print("NN=" + str(len(NN)))

        numberOfMissedNeighbors=(numberOfNeighbors-len(NN))
        if numberOfMissedNeighbors==0:
            distancesMeasured.append(len(NN))
            # distanceVectors.append([getDlsh(point,neighbor,data1.multiplier) for neighbor in NN]) # avstaand till alla grannar
            for neighborNumber,neighbor in enumerate(NN):
                D = getDlsh(point,neighbor,data1.multiplier)
                Dstar = srDistancesVector[i,neighborNumber]
                #print("d=" + str(D) + " d*=" + str(Dstar))
                E += D/Dstar
            numberOfQueriesWithMisses-=1
        # else:
        #     distanceVectors.append(0)
        #     totalNumberOfMissedNeighbors+=numberOfMissedNeighbors
        if(i%100 == 0):
            print("[query] Query point: " + str(i))
    missRatio = float(numberOfQueriesWithMisses)/float(Q)
    E=E/((Q-numberOfQueriesWithMisses)*numberOfNeighbors)
    print("Error: ",E)
    print("Miss ratio: ",missRatio)
    print("Number of distances measured, for all querypoints: ")
    print(distancesMeasured)
    plt.plot(distancesMeasured,'.')
    plt.ylabel("distances measured")
    plt.xlabel("querypoint")
    #plt.hist(distancesMeasured)
    plt.show()
    #getPointDist(queryPoints[0:int(0.2*len(queryPoints))],multiplier

    #print(nearestNeighbors)


if __name__ == '__main__':
    main()
    #linearSearch() # uncomment this line to run the linear search
