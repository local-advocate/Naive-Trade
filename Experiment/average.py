import yfinance as yf
import matplotlib.pyplot as plt

data = []
average = []

def get_data(ticker, period='1d', interval='5m'):
    global data
    company = yf.Ticker(ticker)
    df = company.history(period, interval, actions=False)
    data = df['Open'].to_numpy(dtype=float)    

def algo(n):
    global average, data
    average = data[0]
    sold = False
    i = 1
    boughtArr.append(0)
    while (i < n-1):
        
    return

def make_graph():
    plt.plot(data)
    plt.plot(average, color='b')
    for xc in soldArr:
        plt.axvline(x=xc, color='r', ls='dotted')
    for xc in boughtArr:
        plt.axvline(x=xc, color='g', ls='dotted')
    plt.show()

if __name__ == '__main__':
    get_data('GOOGL', interval='30m')
    algo(data.size)
    make_graph()