import numpy as np

# A smoother and effiecient implementation of sliding window average.
class DataCollector:
    def __init__(self, ticker, interval):      # lower the alpha, the less weight of the previous values
        self.ticker = ticker
        self.interval = interval
        self.data = []

    def gather(self):
        print('Gather data')
        return self.data