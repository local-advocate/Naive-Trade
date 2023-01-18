# Just work with the average.

import yfinance as yf
import matplotlib.pyplot as plt

data = []
averageArr = []

def get_data(ticker, period='1d', interval='5m'):
    global data
    company = yf.Ticker(ticker)
    df = company.history(period, interval, actions=False)
    data = df['Open'].to_numpy(dtype=float)    

def algo(n):
    global average, data
    average = data[0]
    averageSum = data[0]
    averageArr.append(data[0])
    i = 1
    while (i < n-1):
        averageSum += data[i]
        average = averageSum/(i+1)
        averageArr.append(average)
        i += 1
    return

def make_graph():
    plt.plot(averageArr, color='b')
    plt.plot(data, color='g')
    plt.show()

if __name__ == '__main__':
    get_data('GOOGL', interval='1m')
    algo(data.size)
    make_graph()