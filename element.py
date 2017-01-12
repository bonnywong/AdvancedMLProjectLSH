# Earlier version, no longer in use.

import numpy as np


class Element:

    def __init__(self, data):
        print("ay")

    def return_data(self):
        return self.data

    def return_unary(self, c):
        """Returns the unary form of the vector data where the max coordinate
            in the vector space is C"""
        coordinates = []

        for i in range(len(self.data)):
            t = np.zeros(c, dtype=np.int64)
            t[0:self.data[i]] = 1
            t[self.data[i]:c] = 0
            coordinates.append(t)

        return np.concatenate(coordinates)

    def return_hash(self):
        return self.hash_value

    def set_hash(self, hash_value):
        self.hash_value = hash_value