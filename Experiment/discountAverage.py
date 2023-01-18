# Same idea as average, just a smoother average.

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data = []
averageArr = []
invest = 10000          # initial investment
algoInvest = invest
shares = 0
soldArr = []
boughtArr = []

# A smoother and effiecient implementation of sliding window average.
class DiscountedAveragerator:
    def __init__(self, alpha):      # lower the alpha, the less weight of the previous values
        self.alpha = alpha
        self.w = 0.
        self.sum_x = 0.
        self.sum_x_sq = 0.

    def add(self, x):
        self.w = self.alpha * self.w + 1.
        self.sum_x = self.alpha * self.sum_x + x
        self.sum_x_sq = self.alpha * self.sum_x_sq + x * x

    @property
    def avg(self):
        return self.sum_x / self.w

    @property
    def std(self):
        mu = self.avg
        # The np.maximum is purely for safety.
        return np.sqrt(np.maximum(0., self.sum_x_sq / self.w - mu * mu))

# Same algorithm
def algo(n):
    global average, data, invest, algoInvest, shares, soldArr, boughtArr
    averagerator = DiscountedAveragerator(0.8)
    averagerator.add(data[0])
    average = averagerator.avg
    averageArr.append(average)
    
    curr = data[0]
    bought = False
    i = 1
    while (i < n-1):
        curr = data[i]
        # calc new average
        averagerator.add(curr)
        average = averagerator.avg
        averageArr.append(average)
        
        # if curr price < average
        if (curr < average):
            # we have not bought the shares, buy
            if not bought:
                shares = algoInvest/curr            # Total shares = Funds available / current price
                algoInvest = 0
                bought = True
                boughtArr.append(i)
        # curr price > average
        else:
            # if we bought it, sell
            if bought:
                algoInvest = shares*curr            # Available to invest = shares * current price
                shares = 0
                bought = False
                soldArr.append(i)
        i += 1
    return


# Get the data
def get_data(ticker, period='1d', interval='1m'):
    global data
    company = yf.Ticker(ticker)
    df = company.history(period, interval, actions=False)
    data = df['Open'].to_numpy(dtype=float)  

# Make the graph
def make_graph():
    global data, averageArr
    plt.plot(averageArr, color='0', ls='dashed')
    plt.plot(data, color='b')
    for xc in soldArr:
        plt.axvline(x=xc, color='r', ls='dotted')
    for xc in boughtArr:
        plt.axvline(x=xc, color='g', ls='dotted')
    plt.show()
    
# Final stats
def print_stats():
    print('Initial investment($) {}'.format(invest))
    print('Total profit($) {:.2f}'.format(((invest/data[0])*data[-1])-invest))
    if (shares == 0):
        print('Algo profit($) {:.2f}'.format(algoInvest-invest))
    else:
        print('Algo profit($) {:.2f}'.format((shares*data[-1])-invest))
        soldArr.append(len(data)-1)

if __name__ == '__main__':
    get_data('AMZN', interval='1m')
    algo(data.size)
    print_stats()
    make_graph()