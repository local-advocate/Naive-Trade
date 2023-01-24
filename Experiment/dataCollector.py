import yfinance as yf

# A smoother and effiecient implementation of sliding window average.
class DataCollector:
    def __init__(self, ticker, period, interval):      # lower the alpha, the less weight of the previous values
        self.ticker = ticker
        self.interval = interval
        self.period = period
        self.data = []

    def gather(self):
        company = yf.Ticker(self.ticker)
        df = company.history(self.period, self.interval, actions=False)
        self.data = df['Open'].to_numpy(dtype=float)  
