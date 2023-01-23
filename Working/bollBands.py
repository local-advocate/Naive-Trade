# Implementation and visualization of BOLL Bands (+- 2std dev)
import numpy as np
from discountedAverage import DiscountedAveragerator
from dataCollector import DataCollector
import matplotlib.pyplot as plt


# The moving average algorithm
class BollBands():
    def __init__(self, data, times, alpha):
        self.data = data
        self.averagerator = DiscountedAveragerator(alpha=alpha)
        self.upper = []
        self.lower = []
        self.average = []
        self.times = times
    
    def algo(self):
        # Compare against data[0]
        self.averagerator.add(self.data[0])
        self.average.append(self.averagerator.avg)
        self.upper.append(self.averagerator.avg + self.times * self.averagerator.std)
        self.lower.append(self.averagerator.avg - self.times * self.averagerator.std)
        
        # Initialize variables
        bought = False
        i = 1
        n = len(self.data)
        
        while (i < n-1):
            curr = self.data[i]
            # calc new average
            self.averagerator.add(curr)
            average = self.averagerator.avg
            deviation = self.averagerator.std
            self.average.append(average)
            self.upper.append(average + self.times * deviation)
            self.lower.append(average - self.times * deviation)
            i += 1
        return
    
    def graph(self):
        plt.plot(self.data, color='b')                       # plot data
        plt.plot(self.average, color='m')                    # plot average
        plt.plot(self.upper)                      # plot upper band
        plt.plot(self.lower)                      # plot lower band
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
    boll = BollBands(data=collector.data, times=2, alpha=0.8)
    boll.algo()
    boll.graph()
    