# Make trades looking at trends (sell if downwards, buy if upwards).
# https://en.wikipedia.org/wiki/Linear_trend_estimation
# https://stackoverflow.com/questions/20329545/how-to-check-if-a-sequence-of-numbers-has-a-increasing-decreasing-trend-in-c

import numpy as np
from discountedAverage import DiscountedAveragerator
from dataCollector import DataCollector
from grapher import Grapher

# The moving average algorithm
class FollowTrend():
    def __init__(self, data, alpha, invest, buyPoints):
        self.data = data
        self.averagerator = DiscountedAveragerator(alpha=alpha)
        self.sell = []
        self.buy = []
        self.average = []
        self.shares = 0
        self.invest = invest
        self.algoInvest = self.invest
        self.stat = ''
        self.buyPoints = buyPoints
        self.boughtPrice = 0
        
    def algo(self):
        
        # watch initial points
        for i in range(self.buyPoints):
            self.averagerator.add(self.data[i])
            self.average.append(self.averagerator.avg)
        
        # Initialize variables
        bought = False
        i = self.buyPoints
        n = len(self.data)
        
        while (i < n-1):
            # calc new average
            curr = self.data[i]
            self.averagerator.add(curr)
            average = self.averagerator.avg
            self.average.append(average)
            
            # average decreasing, sell if bought
            if (bought and curr > self.boughtPrice and average < self.average[-2]):
                self.algoInvest = self.shares*curr            # Available to invest = shares * current price
                self.shares = 0
                bought = False
                self.sell.append(i)
            # average increasing trend, and not bought
            elif (not bought and average > self.average[-self.buyPoints]):
                self.shares = self.algoInvest/curr            # Total shares = Funds available / current price
                self.algoInvest = 0
                bought = True
                self.buy.append(i)
                self.boughtPrice = curr
            i += 1
        return

    def stats(self):
        self.stat += 'Initial investment($) {}\n'.format(self.invest)
        print('Initial investment($) {}'.format(self.invest))
        # Buy at the beginning, self at the end price
        self.stat += 'Total profit($) {:.2f}\n'.format(((self.invest/self.data[0])*self.data[-1])-self.invest)
        print('Total profit($) {:.2f}'.format(((self.invest/self.data[0])*self.data[-1])-self.invest))
        # All shares sold, remaining value v. what we started with
        if (self.shares == 0):
            self.stat += 'Algo profit($) {:.2f}\n'.format(self.algoInvest-self.invest)
            print('Algo profit($) {:.2f}'.format(self.algoInvest-self.invest))
        # Shares remaining
        else:
            self.stat += 'Shares remaining {:.2f}\n'.format(self.shares)
            self.stat += 'Profit($) {:.2f}\n'.format(self.boughtPrice*self.shares - self.invest)
            print('Shares remaining {:.2f}'.format(self.shares))
            print('Profit($) {:.2f}\n'.format(self.boughtPrice*self.shares - self.invest))
        
if __name__ == '__main__':
    # Company and Investment Info
    info = {
        'company': 'NVDA',
        'period' : '1d',
        'interval': '1m',
        'invest': 10000
    }
    
    # Collect data
    collector = DataCollector(ticker=info['company'], period=info['period'], interval=info['interval'])
    collector.gather()
    
    # Run Algo & Print Stats
    ft = FollowTrend(data=collector.data, alpha=0.8, invest=info['invest'], buyPoints=3)
    ft.algo()
    ft.stats()
    
    # Graph the results
    grapher = Grapher(data=collector.data, average=ft.average, sell=ft.sell, buy=ft.buy, stats=ft.stat)
    grapher.graphit()