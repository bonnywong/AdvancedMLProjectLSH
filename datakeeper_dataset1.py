from parse import parse_dataset
from hashtable import HashTable
import numpy as np
import time


class Datakeeper:

    def __init__(self,numberOfHashtables,dataset1_filename="Dataset_1_short.rcd"):
        # Import dataset_1:
        # dataset1 is a list of points (each point is a numpy array, its elements are the coordinates)
        # in rest of code, all points can be referenced by their index in dataset1
        t = time.process_time()
        self.dataset1,self.dataset1_dimension = parse_dataset(dataset1_filename)
        delta_t = time.process_time() - t
        print("Took:", delta_t, "seconds to parse", dataset1_filename)

        #skapa hashtabeller
        C = 0
        for i in self.dataset1:
            npmax = np.max(i)
            if npmax>C:
                C = npmax
        M = 1000
        k = 700
        bucketSize = 300
        hashtables=list()
        for i in range(numberOfHashtables):
            hashtables.append(HashTable(M,k,self.dataset1_dimension,bucketSize,C,self))
        hashtables[0].add_point(0)

    def getBuckets(self,queryPoint):
        pass

    def getPoint(self,pointIndex):
        #return self.dataset1[pointIndex]
        #OBS!  byt tillbaka här sen!!!
        return self.dataset1[0]


def main():
    data1 = Datakeeper(numberOfHashtables=3)






if __name__ == '__main__':
    main()