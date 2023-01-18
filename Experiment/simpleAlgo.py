# Detect peaks and valleys

import numpy as np

np.set_printoptions(precision=2)

# array to store all the data
data = []
profitArr = []
invest = 10000          # initial investment
buyPrice = 0
sellPrice = 0
algoInvest = invest
shares = 0

# generate random floats array of n points
def generate_data(fromm, to, n):
    global data, profitArr
    data = (fromm-to) * np.random.random(n) + to

def algo(n):
    global data, algoInvest, shares
    tracker = data[0]
    sold = False
    shares = algoInvest / data[0]                   # Initial shares bought @ data[0]
    i = 1
    pArr = []
    while (i < n-1):
        curr = data[i]
        tracker = data[i-1]
        # If the latest data is less than previous data point
        if (curr < tracker):
            # and we are not all sold already
            if not sold:
                #print('S-{0}-{1}'.format(i, curr))  
                algoInvest = shares*curr            # Available to invest = shares * current price
                shares = 0
                sold = True
                profitArr.append(pArr)
                pArr = []
        
        # current price more than previous one
        else:
            pArr.append(curr)
            # and we have not bought it already
            if sold:
                #print('B-{0}-{1}'.format(i, curr))
                shares = algoInvest/curr            # Total shares = Funds available / current price
                algoInvest = 0
                sold = False
        i += 1
    return
        
def print_stats(n):
    print('Price array: ', data)
    print('Profit array: ', profitArr)
    print('Initial investment($) {}'.format(invest))
    print('Total profit($) {:.2f}'.format(((invest/data[0])*data[n-1])-invest))
    if (shares == 0):
        print('Algo profit($) {:.2f}'.format(algoInvest-invest))
    else:
        print('Algo profit($) {:.2f}'.format((shares*data[n-1])-invest))
    return
    
if __name__ == '__main__':
    fromm, to, n = 0, 100, 1000
    endPrice = (fromm-to) * np.random.random() + to
    generate_data(fromm, to, n)
    algo(n)
    print_stats(n)