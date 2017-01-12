# Earlier version, no longer in use.

import bitarray
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from bucket import Bucket


def hamming_distance(x, y):
    assert len(x) == len(y)
    dist = 0
    for xi, yi in zip(x, y):
        if xi != yi:
            dist += 1

    return dist

# Do it mathematically.
def to_unary(data, C):
    """Returns the unary form of the vector data where the max coordinate
    in the vector space is C"""
    coordinates = []

    for i in range(len(data)):
        t = np.zeros(C, dtype=np.int64)
        t[0:data[i]] = 1
        t[data[i]:C] = 0
        coordinates.append(t)

    return np.concatenate(coordinates)


def gen_data(min_coord, max_coord, size):
    """Returns a list of length 'size' of random uniformly distributed
    integers between the range min_coord and max_coord"""
    data = np.random.randint(min_coord, max_coord, size)
    return data


a = '123345'
b = "123353"
dist = hamming_distance(a, b)
print("Hamming distance between: ", a, "and", b, " = ", dist)

# Swedish 3-letter words
sv_words = ['väg', 'tar', 'hej', 'apa', 'åar', 'mår', 'bra', 'tja']

# English 3-letter words
en_words = ['bat', 'bar', 'sup', 'car', 'bit', 'cop', 'man', 'sad']

ba = bitarray.bitarray()

print(ba.fromstring(a))

k = 10
dims = 64
b1 = Bucket(1, dims, k, 50)
hashes = np.random.randint(0, dims, k)
print(hashes)

# Generate some random separable 3-dimensional data

# data set a
data_x_a = gen_data(10, 15, 20)
data_y_a = gen_data(10, 15, 20)
data_z_a = gen_data(10, 15, 20)

# data set b
data_x_b = gen_data(35, 45, 20)
data_y_b = gen_data(35, 45, 20)
data_z_b = gen_data(5, 20, 20)

# data set c
data_x_c = gen_data(15, 20, 20)
data_y_c = gen_data(15, 20, 20)
data_z_c = gen_data(15, 20, 20)

# data set d
data_x_d = gen_data(30, 45, 20)
data_y_d = gen_data(15, 45, 20)
data_z_d = gen_data(15, 45, 20)

plot_data = False
if plot_data:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(data_x_a, data_y_a, data_z_a, c='r', marker='o')
    ax.scatter(data_x_b, data_y_b, data_z_b, c='g', marker='o')
    ax.scatter(data_x_c, data_y_c, data_z_c, c='b', marker='o')
    ax.scatter(data_x_d, data_y_d, data_z_d, c='y', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

dims = 3
k = 20
bucket_size = 50
C = 45
bucket_a = Bucket(1, C, k, bucket_size)
bucket_b = Bucket(2, C, k, bucket_size)
bucket_c = Bucket(3, C, k, bucket_size)
bucket_d = Bucket(4, C, k, bucket_size)

# Zipping datasets a, b, c and d
data_a = list(zip(data_x_a, data_y_a, data_z_a))
data_b = list(zip(data_x_b, data_y_b, data_z_b))
data_c = list(zip(data_x_c, data_y_c, data_z_c))
data_d = list(zip(data_x_d, data_y_d, data_z_d))
print("Zipped dataset: ", (data_d))

# Note the hash is the bucket!

for tuple in data_d:
    #print("Tuple: ", tuple)
    #print("Unary form: ", to_unary(tuple, 45))
    hash_a = bucket_a.hash_element(to_unary(tuple, 45))
    # hash_b = bucket_b.hash_element(to_unary(tuple, 45))
    # hash_c = bucket_c.hash_element(to_unary(tuple, 45))
    # hash_d = bucket_d.hash_element(to_unary(tuple, 45))

    print(hash_a)