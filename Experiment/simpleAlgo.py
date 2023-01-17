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
    tracker = data[0]
    sold = False
    i = 1
    while (i < n):
        curr = data[i]
        tracker = data[i-1]
        # If the latest data is less than previous data point
        if (curr < tracker):
            # and we are not all sold already
            if not sold:
                print('S-{0}-{1}'.format(i, curr))
                sold = True
        
        # current price more than previous one
        else:
            # and we have not bought it already
            if sold:
                print('B-{0}-{1}'.format(i, curr))
                sold = False
        i += 1
        
if __name__ == '__main__':
    fromm, to, n = 90, 100, 20
    generate_data(fromm, to, n)
    algo(n)
    print(data)