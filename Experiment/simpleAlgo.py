# Detect peaks and valleys

import numpy as np

np.set_printoptions(precision=2)

# array to store all the data
data = []
profitArr = []

# generate random floats array of n points
def generate_data(fromm, to, n):
    global data
    data = (fromm-to) * np.random.random(n) + to

def algo(n):
    global data
    i = 0
    while i < n-1:
        pArr = []
        while (i < n-1 and data[i] < data[i+1]):
            pArr.append(data[i])
            i += 1
        profitArr.append(pArr)
        print('Sell at ', i, '---', data[i])
        while (i < n-1 and data[i] > data[i+1]):
            i += 1
        print('Buy at ', i, '---', data[i])
    print(data, n)
    print(profitArr)
        
if __name__ == '__main__':
    fromm, to, n = 90, 100, 20
    generate_data(fromm, to, n)
    algo(n)