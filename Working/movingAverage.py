import numpy as np
from discountedAverage import DiscountedAveragerator
from dataCollector import DataCollector
from grapher import Grapher



if __name__ == '__main__':
    info = {
        'company': 'AMZN',
        'period' : '1d',
        'interval': '1m'
    }
    averagerator = DiscountedAveragerator(0.8)      # accurate alpha
    collector = DataCollector(ticker=info['company'], period=info['period'], interval=info['interval'])
    collector.gather()
    grapher = Grapher(data=collector.data)
    grapher.graphit()