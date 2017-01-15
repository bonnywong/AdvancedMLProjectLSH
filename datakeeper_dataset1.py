from parse import parse_dataset
from hashtable import HashTable
import numpy as np
import pickle
import time
import matplotlib.pyplot as plt


class Datakeeper:

    def __init__(self,dataset1_filename="Dataset_1_data.rcd"):
        # Import dataset_1:
        # dataset1 is a list of points (each point is a numpy array, its elements are the coordinates)
        # in rest of code, all points can be referenced by their index in dataset1
        #t = time.process_time()
        self.multiplier = 1 #1000000
        self.translation = 0 #2.5
        self.dataset1,self.dataset1_dimension = parse_dataset(dataset1_filename,self.multiplier,self.translation)
        #delta_t = time.process_time() - t
        #print("Took:", delta_t, "seconds to parse", dataset1_filename)


        #change dataset
        '''
        for i in range(len(self.dataset1)):
            for j in range(len(self.dataset1[i])):
                self.dataset1[i][j] = np.random.randint(255, size = 1)
        '''

        #skapa hashtabeller
        numberOfHashtables=7 # deras notation: l
        M = 151 # size of hashtable
        k = 700 # number of Hamming indices included in each g_i
        bucketSize = 250 # Size of buckets

        C = 0
        for i in self.dataset1:
            npmax = np.max(i)
            if npmax>C:
                C = npmax
        self.hashtables=list()
        for i in range(numberOfHashtables):
            self.hashtables.append(HashTable(M,k,self.dataset1_dimension,bucketSize,C,self))

        
        for i in range(len(self.dataset1)):
            for h in self.hashtables:
                h.add_point(i)
            if(i%100 == 0):
                print("Point: " + str(i))
        
        
        '''
        for i in self.hashtables:
            i.add_point(0)
            i.add_point(1)
            i.add_point(1)
            i.add_point(2)

        queryPoint = self.getPoint(3)
        print("\nqueryPoint: \n" + str(queryPoint))
        print("neighbours: \n" + str(self.getNN(queryPoint,700)))
        '''

    def getBuckets(self,queryPoint):
        S = []
        for i in self.hashtables:
            S.append(i.get_bucket(queryPoint))
        return S

    def getPoint(self,pointIndex):
        return self.dataset1[int(pointIndex)] #omotiverad typecastning! var foersiktig!

    def getNN(self,point,K):
        S = np.unique(np.concatenate(self.getBuckets(point)))
        S.astype(int)
        #print(type(S))
        #print(type(S[199]))
        #S = [int(x) for x in S]
        distance = np.zeros(S.size)
        for i in range(S.size):
            distance[i] = np.linalg.norm(point-np.array(self.getPoint(S[i])))
        index = sorted(range(len(distance)), key=lambda k: distance[k])
        S_sorted = S[index]

        P = list()
        for i in range(min(S.size,K)):
            P.append(self.getPoint(S_sorted[i]))
        return P


def saveData(data,filename="default"):
    with open('exported/'+filename, 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)
    print("[datakeeper] Data saved as: exported/"+filename)


def loadData(filename="default"):
    print("[datakeeper] Loading object: exported/"+filename)
    with open('exported/'+filename, 'rb') as input:
        data = pickle.load(input)
    print("[datakeeper] Done loading")
    return data


def main():

    data1 = Datakeeper(dataset1_filename="d1/Dataset_1_Homemade_data.rcd")
    saveData(data=data1,filename="temp1")

    total = np.zeros(len(data1.dataset1))
    for table in range(len(data1.hashtables)):
        hashes = np.zeros(len(data1.dataset1))
        for i in range(len(data1.dataset1)):
            hashes[i] = data1.hashtables[table].LSH(data1.getPoint(i))
        plt.figure(table+1)
        plt.subplot(211)
        plt.plot(hashes)
        plt.subplot(212)
        plt.hist(hashes, data1.hashtables[table].M, facecolor='green', alpha=1)
        total = total + hashes



    #Information about dataset
    plt.figure(len(data1.hashtables)+1)
    alldata = np.array(data1.dataset1)
    alldata = np.reshape(alldata,(len(data1.dataset1)*data1.dataset1_dimension,1))
    plt.hist(alldata, 257, facecolor='green', alpha=1)

    #plt.figure(len(data1.hashtables)+1)
    #plt.plot(total/len(data1.dataset1))
    #plt.hist(total/len(data1.dataset1), 20, facecolor='green', alpha=1)
    plt.show()

    '''
    for i in range(len(data1.hashtables)):
        plt.figure(i+1)
        b = np.zeros(data1.hashtables[i].M)
        #print(b.size)
        for j in range(data1.hashtables[i].M):
            b[j] = len(data1.hashtables[i].table[j])
            #print(b[j])
        ax = plt.subplot(311)
        ax.bar(range(len(b)), b)
        plt.subplot(312)
        plt.hist(data1.hashtables[i].hash_index, 20, facecolor='green', alpha=1)
        #plt.plot(data1.hashtables[i].hash_index)
        plt.subplot(313)
        plt.hist(data1.hashtables[i].hash_const, 20, facecolor='green', alpha=1)
        #plt.plot(data1.hashtables[i].hash_const)
        #plt.plot(b)
    plt.show()
    '''

    #del data1


    '''
    #Load test
    data1b=loadData(filename="temp1")

    print("Find NN")
    print(data1b.getNN(data1b.getPoint(3),1))
    '''




if __name__ == '__main__':
    main()
