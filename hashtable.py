import numpy as np


class HashTable:

    def __init__(self, size,maxb,maxp):
        print("Init hashtable")
        dims = 4
        self.M = size
        self.C = maxp
        self.bucketSize = maxb

        self.hash_index = np.random.randint(maxp,size=5)
        self.hash_const = np.random.randint(self.M-1,size=5)
        self.table = np.empty((self.M), dtype=object)
        for i in range(self.M):
            self.table[i] = []

    def LSH(self,point):
        """Hash function without converting to unary"""
        h = 0;
        for i in range(point.size):
            if(self.hash_index[i]%self.C < point[self.hash_index[i]//self.C]):
                h += self.hash_const[i]
        return h % self.M

    def add_point(self,point):
        index = self.LSH(point)
        if (len(self.table[index]) < self.bucketSize):
            self.table[self.LSH(point)].append(point)
        print(self.table)

    def get_bucket(self,point):
        return self.table[self.LSH(point)]


# Hashtable(M,B,C)
# M = size of hashtalbe
# B = max size of buckets
# C = largest number in dataset
H = HashTable(10,2,2)

point = np.array([1,2,1])
point2 = np.array([2,1,2])

print("Add points")
H.add_point(point)
H.add_point(point2)

print("Bucket:")
print(H.get_bucket(point))

print('hash')
print(H.LSH(point))
