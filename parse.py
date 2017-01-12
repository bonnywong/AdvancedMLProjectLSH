# Parse from file, return it as tuple (see below) (for use in other functions)
# Initial code written by Bonny

import numpy as np
import time

#  It is assumed that the dataset is in the root of
#  working dir.
def parse_dataset(filename):
    data = []
    file = open(filename, 'r')
    dimension = file.readline()
    print(dimension)

    counter = 0
    for line in file:
        #line = file.readline()
        p = line.strip().split(":")
        p.pop()  # Removes the last element that gives us the index of the point.
        p = list(map(np.float, p))  # Convert string to numpy floats

        data.append(p)

        counter += 1
        if counter % 10 == 0:
            print("Elements:", counter, end='\r')

    print("Elements:", counter)
    return data, dimension  #OBS! Note that we're returning a tuple.

dataset1 = "Dataset_1.rcd"

t = time.process_time()
data, data_dim = parse_dataset(dataset1)
delta_t = time.process_time() - t

print("Took:", delta_t, "seconds to parse", dataset1)

for i in range(5):
    print(data[i])