import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data = []
averageArr = []

# A smoother and effiecient implementation of sliding window average.
class DiscountedAveragerator:
    def __init__(self, alpha):
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
    plt.show()

if __name__ == '__main__':
    get_data('AMZN')
    averagerator = DiscountedAveragerator(0.9)
    for d in data:
        averagerator.add(d)
        averageArr.append(averagerator.avg)   
    make_graph()