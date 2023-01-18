import yfinance as yf
import matplotlib.pyplot as plt

data = []
invest = 10000          # initial investment
algoInvest = invest
shares = 0
soldArr = []
boughtArr = []

def get_data(ticker, period='1d', interval='5m'):
    global data
    company = yf.Ticker(ticker)
    df = company.history(period, interval, actions=False)
    data = df['Open'].to_numpy(dtype=float)
    

def algo(n):
    global invest, algoInvest, shares, soldArr, boughtArr
    buyPrice = data[0]
    tracker = data[0]
    sold = False
    shares = algoInvest / data[0]                   # Initial shares bought @ data[0]
    i = 1
    boughtArr.append(0)
    while (i < n-1):
        curr = data[i]
        tracker = data[i-1]
        if (curr < tracker):
            if not sold:
                # print('S-{0}-{1}'.format(i, curr))
                algoInvest = shares*curr            # Available to invest = shares * current price
                shares = 0
                sold = True
                soldArr.append(i)
        else:
            if sold:
                # print('B-{0}-{1}'.format(i, curr))
                shares = algoInvest/curr            # Total shares = Funds available / current price
                algoInvest = 0
                sold = False
                buyPrice = curr
                boughtArr.append(i)
        i += 1
    soldArr.append(i)
    return

def print_stats():
    print('Initial investment($) {}'.format(invest))
    print('Total profit($) {:.2f}'.format(((invest/data[0])*data[-1])-invest))
    if (shares == 0):
        print('Algo profit($) {:.2f}'.format(algoInvest-invest))
    else:
        print('Algo profit($) {:.2f}'.format((shares*data[-1])-invest))

def make_graph():
    plt.plot(data)
    for xc in soldArr:
        plt.axvline(x=xc, color='r', ls='dotted')
    for xc in boughtArr:
        plt.axvline(x=xc, color='g', ls='dotted')
    plt.show()

if __name__ == '__main__':
    get_data('AMZN', interval='5m')
    algo(data.size)
    print_stats()
    make_graph()