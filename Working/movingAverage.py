import numpy as np
from discountedAverage import DiscountedAveragerator
from dataCollector import DataCollector
from grapher import Grapher

# The moving average algorithm
class MovingAverage():
    def __init__(self, data, alpha):
        self.data = data
        self.averagerator = DiscountedAveragerator(0.8)
        self.sell = []
        self.buy = []
        self.average = []
    
    def algo(self):
        print('MA Algo')
        for d in self.data:
            self.averagerator.add(d)
            self.average.append(self.averagerator.avg)

    def stats(self):
        print('MA Stats')

if __name__ == '__main__':
    # Company Info
    info = {
        'company': 'AMZN',
        'period' : '1d',
        'interval': '1m'
    }
    
    # Collect data
    collector = DataCollector(ticker=info['company'], period=info['period'], interval=info['interval'])
    collector.gather()
    
    # Run Algo & Print Stats
    mavg = MovingAverage(data=collector.data, alpha=0.8)
    mavg.algo()
    mavg.stats()
    
    # Graph the results
    grapher = Grapher(data=collector.data, average=mavg.average)
    grapher.graphit()