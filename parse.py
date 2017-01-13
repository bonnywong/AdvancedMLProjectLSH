# Parse from file, return it as tuple (see below) (for use in other functions)
# Initial code written by Bonny

import numpy as np
import time
from hashtable import HashTable

#  It is assumed that the dataset is in the root of
#  working dir.
def parse_dataset(filename,multiplier,translation):
    data = []
    file = open(filename, 'r')
    dimension = int(file.readline())
    print("[Parsing] Dimension: ",dimension)

    counter = 0
    for line in file:
        #line = file.readline()
        p = line.strip().split(":")
        p.pop()  # Removes the last element that gives us the index of the point.
        p = list(map(np.float, p))  # Convert string to numpy floats
        p = [(x+translation)*multiplier for x in p]
        #p = np.array(p)

        data.append(p)

        counter += 1
        #if counter % 10 == 0:
        #    print("Elements:", counter, end='\r')

    print("[Parsing] Number of elements parsed from ("+filename+"): ", counter)
    return data, dimension  #OBS! Note that we're returning a tuple.
    # data is a list of numpy arrays (of coordinates)

def main():

    dataset1 = "Dataset_1_data.rcd"

    #t = time.process_time()
    data, data_dim = parse_dataset(dataset1)
    #delta_t = time.process_time() - t

    #print("Took:", delta_t, "seconds to parse", dataset1)

    for i in range(5):
        print(data[i])

if __name__ == '__main__':
        main()
