# Earlier version, no longer in use.

import numpy as np


#  l = length of the hash table
#  c = the largest coordinate that exists among all the data
#  k = width of the hash function
def pre_process(l, c, k):
    hash_table = []

    for i in range(l):
        hash_function = np.random.randint(0, c, k)
        hash_table.append(hash_function)

    #  hash_table is just a list consisting of vectors with
    #  random numbers, these vectors are our "hash" functions
    return hash_table


def to_unary(data, c):
    """Returns the unary form of the vector data where the largest coordinate
    used in the vector space is C"""
    coordinates = []

    for i in range(len(data)):
        t = np.zeros(c, dtype=np.int64)  # I'm using integers
        t[0:data[i]] = 1
        t[data[i]:c] = 0
        coordinates.append(t)

    return np.concatenate(coordinates)


def hash_point(p, hash_func, c):
    hash_value = []

    unary_p = to_unary(p, c)
    for x in hash_func:
        hash_value.append(unary_p[x])

    return hash_value


def gen_data(min_coord, max_coord, size):
    """Returns a list of length 'size' of random uniformly distributed
    integers between the range min_coord and max_coord"""
    data = np.random.randint(min_coord, max_coord, size)
    return data


def parse_data():
    return 0


def store_points(l, n, hash_table, data, c):
    for hash_func in hash_table:
        for n in range(n):
            h = hash_point(data[n], hash_func, c)
            print("Hash value: ", h)


def main():
    l = 10
    c = 100
    k = 10
    hash_table = pre_process(l, c, k)

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

    data_a = list(zip(data_x_a, data_y_a, data_z_a))
    data_b = list(zip(data_x_b, data_y_b, data_z_b))
    data_c = list(zip(data_x_c, data_y_c, data_z_c))
    data_d = list(zip(data_x_d, data_y_d, data_z_d))

    store_points(l, len(data_a), hash_table, data_a, c)
    print("Hash table: ", hash_table)
    return 0

if __name__ == "__main__":
    main()
