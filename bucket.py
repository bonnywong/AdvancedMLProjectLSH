# Earlier version, no longer in use.

import numpy as np


class Bucket:
    elements = []

    def __init__(self, bucket_id, C, k, bucket_size):
        self.bucket_id = bucket_id;
        self.hashes = np.random.randint(0, C, k)
        self.bucket_size = bucket_size;
        print("Bucket with ID:", self.bucket_id, "created.")
        print("Hash functions: ", self.hashes)

    def hash_element(self, element):
        hash = []
        for x in self.hashes:
            hash.append(element[x])
        return hash

    def contains(self, element):
        return 0

    def add(self, element):
        return 0

    def remove(self, element):
        return 0

    def return_hashes(self):
        return self.hashes

    def return_id(self):
        return id

    def display_id(self):
        print("Bucket-ID:", id)