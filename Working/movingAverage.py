import numpy as np
from discountedAverage import DiscountedAveragerator
from dataCollector import DataCollector
from grapher import Grapher

# The moving average algorithm
class MovingAverage():
    def __init__(self, data, alpha, invest):
        self.data = data
        self.averagerator = DiscountedAveragerator(alpha=alpha)
        self.sell = []
        self.buy = []
        self.average = []
        self.shares = 0
        self.invest = invest
        self.algoInvest = self.invest
    
    def algo(self):
        # Compare against data[0]
        self.averagerator.add(self.data[0])
        self.average.append(self.averagerator.avg)
        average = self.averagerator.avg                 # Ongoing average value
        
        # Initialize variables
        bought = False
        i = 1
        n = len(self.data)
        
        while (i < n-1):
            curr = self.data[i]
            # calc new average
            self.averagerator.add(curr)
            average = self.averagerator.avg
            self.average.append(average)
            
            # if curr price < average
            if (curr < average):
                # we have not bought the shares, buy
                if not bought:
                    self.shares = self.algoInvest/curr            # Total shares = Funds available / current price
                    self.algoInvest = 0
                    bought = True
                    self.buy.append(i)
            # curr price > average
            else:
                # if we bought it, sell
                if bought:
                    self.algoInvest = self.shares*curr            # Available to invest = shares * current price
                    self.shares = 0
                    bought = False
                    self.sell.append(i)
            i += 1
        return

    def stats(self):
        print('Initial investment($) {}'.format(self.invest))
        # Buy at the beginning, self at the end price
        print('Total profit($) {:.2f}'.format(((self.invest/self.data[0])*self.data[-1])-self.invest))
        # All shares sold, remaining value v. what we started with
        if (self.shares == 0):
            print('Algo profit($) {:.2f}'.format(self.algoInvest-self.invest))
        # Shares remaining, sold at the end price
        else:
            print('Algo profit($) {:.2f}'.format((self.shares*self.data[-1])-self.invest))
            self.sell.append(len(self.data)-1)

if __name__ == '__main__':
    # Company and Investment Info
    info = {
        'company': 'AMZN',
        'period' : '1d',
        'interval': '1m',
        'invest': 10000
    }
    
    # Collect data
    collector = DataCollector(ticker=info['company'], period=info['period'], interval=info['interval'])
    collector.gather()
    
    # Run Algo & Print Stats
    mavg = MovingAverage(data=collector.data, alpha=0.8, invest=info['invest'])
    mavg.algo()
    mavg.stats()
    
    # Graph the results
    grapher = Grapher(data=collector.data, average=mavg.average, sell=mavg.sell, buy=mavg.buy)
    grapher.graphit()