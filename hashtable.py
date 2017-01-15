import numpy as np
#from datakeeper_dataset1 import Datakeeper

class HashTable:

    def __init__(self,size,k,dim,maxb,maxp,datakeeper):
        print("Init hashtable")
        self.M = size
        self.C = maxp
        self.bucketSize = maxb
        self.datakeeper = datakeeper

        self.hash_index = np.random.randint(self.C*dim,size=k)
        self.hash_const = np.random.randint(self.M-1,size=k)
        #print(self.hash_const)
        #self.hash_const.tofile('foo.csv',sep=',',format='%10.5f')
        #np.random.randint(self.M-1,size=k)
        self.table = np.empty((self.M), dtype=object)
        for i in range(self.M):
            self.table[i] = []

    def LSH(self,point):
        """Hash function without converting to unary"""
        h = 0;
        for i in range(len(point)):
            if(point[int(self.hash_index[i]//self.C)] > self.hash_index[i]%self.C):
                h+=self.hash_const[i]
        return h % self.M

    def add_point(self,pointIndex):
        point = self.datakeeper.getPoint(pointIndex)
        index = self.LSH(point)
        if (len(self.table[index]) < self.bucketSize):
            self.table[index].append(pointIndex)
            #print("Bucket: " + str(self.table[index]))
        '''
        else:
            #print("Bucket full: hash="+str(index) + " point[0]=" + str(point[0]))
            
            for i in range(1,self.M):
                index=index+1
                if (len(self.table[(index)%self.M]) < self.bucketSize):
                    self.table[(index)%self.M].append(pointIndex)
                    return
'''
    def get_bucket(self,point):
        return self.table[self.LSH(point)]

def main():
    #OBS! detta kommer inte att fungera nu langre, eftersom HashTable ar andrad.

    # Hashtable(M,k,dim,B,C)
    # M = size of hashtalbe
    # k = dimensions for g and a (number of bits to use from unary array)
    # dim = dimensions of the data
    # B = max size of buckets
    # C = largest number in dataset
    H = HashTable(10,5,1,2)

    point = np.array([1,2,1])
    point2 = np.array([2,1,2])

    print("Add points")
    H.add_point(point)
    H.add_point(point2)

    print("Bucket:")
    print(H.get_bucket(point))

    print('hash')
    print(H.LSH(point))


if __name__ == '__main__':
    main()
