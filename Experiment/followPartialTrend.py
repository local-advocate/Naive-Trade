# Make trades looking at trends (sell if downwards, buy if upwards).
# https://en.wikipedia.org/wiki/Linear_trend_estimation
# https://stackoverflow.com/questions/20329545/how-to-check-if-a-sequence-of-numbers-has-a-increasing-decreasing-trend-in-c

import numpy as np
from DiscountedAveragerator import DiscountedAveragerator
from dataCollector import DataCollector
from grapher import Grapher
from matplotlib import pyplot as plt
import math

class FollowPartialTrend():
    def __init__(self, data, alpha, invest, buyPoints, split):
        self.data = data
        self.averagerator = DiscountedAveragerator(alpha=alpha)
        self.sell = []
        self.buy = []
        self.average = []
        self.invest = invest
        self.stat = ''
        self.buyPoints = buyPoints
        self.split = split
        self.totalProfit = 0
        self.totalShares = 0
        
    def inject(self, amount, start):
        n = len(self.data)
        shares = 0
        bought = False
        boughtPrice = 0
        profit = 0
        while (start < n):
            curr = self.data[start]
            # average decreasing, sell if bought
            if (bought and curr > boughtPrice and self.average[start] < self.average[start-1]):
                amount = shares*curr            # Available to invest = shares * current price
                shares = 0
                bought = False
                self.sell.append(start)
            # average increasing trend, and not bought
            elif (not bought and self.average[start] > self.average[start-self.buyPoints]):
                shares = amount/curr            # Total shares = Funds available / current price
                profit = amount - (self.invest/self.split)
                amount = 0
                bought = True
                self.buy.append(start)
                boughtPrice = curr
            start += 1
        return {'profit': profit, 'shares': shares}
    
    
    def calculate_avg(self):
        # Compare against data[0]
        self.averagerator.add(self.data[0])
        self.average.append(self.averagerator.avg)
        average = self.averagerator.avg                 # Ongoing average value
        # Initialize variables
        i = 1
        n = len(self.data)
        while (i < n):
            curr = self.data[i]
            # calc new average
            self.averagerator.add(curr)
            average = self.averagerator.avg
            self.average.append(average)
            i += 1
        return
    
    def algo(self):
        self.calculate_avg()
        start = self.buyPoints
        amount = self.invest/self.split
        length = len(self.data)
        for _ in range(self.split):
            res = self.inject(amount=amount, start=start)
            self.totalProfit += res['profit']
            self.totalShares += res['shares']
            start += math.ceil(length/self.split)
            # print('Start: {:.2f}. Amount: {:.2f}. Profit: {:.2f}. Shares: {:.2f}.'.format(start, amount, res['profit'], res['shares']))
        return
    
    def stats(self):
        self.stat += 'Initial investment($) {}\n'.format(self.invest)
        print('Initial investment($) {}'.format(self.invest))
        # Buy at the beginning, self at the end price
        self.stat += 'Total profit($) {:.2f}\n'.format(((self.invest/self.data[0])*self.data[-1])-self.invest)
        print('Total profit($) {:.2f}'.format(((self.invest/self.data[0])*self.data[-1])-self.invest))
        # All shares sold, remaining value v. what we started with
        self.stat += 'Shares remaining {:.2f}\n'.format(self.totalShares)
        self.stat += 'Algo Profit($) {:.2f}\n'.format(self.totalProfit)
        print('Shares remaining {:.2f}'.format(self.totalShares))
        print('Algo Profit($) {:.2f}\n'.format(self.totalProfit))
        
    def graph(self):
        plt.figure()
        plt.xlim(0, len(self.data))
        plt.plot(self.data, color='b')                                    # plot data
        plt.plot(self.average, color='m', ls='dashed')                    # plot average
        for xc in self.sell:
            plt.plot(xc, self.data[xc], 'ro', markersize=4)
        for xc in self.buy:
            plt.plot(xc, self.data[xc], 'go', markersize=4)
        start = self.buyPoints
        length = len(self.data)
        splitArr = []
        for _ in range(self.split):
            splitArr.append(start)
            start += math.ceil(length/self.split)
        for xc in splitArr:
            plt.axvline(x=xc, color='c', ls='dotted')
        plt.annotate(text=self.stat, xy=(0.4, 0.9), xycoords='axes fraction',
                    family='cursive', size='smaller', bbox={'boxstyle':'round'})
        plt.show()
        
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
    ft = FollowPartialTrend(data=collector.data, alpha=0.8, invest=info['invest'], buyPoints=3, split=100)
    ft.algo()
    ft.stats()
    ft.graph()
