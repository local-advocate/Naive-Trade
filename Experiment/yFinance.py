import yfinance as yf
import matplotlib.pyplot as plt

amazon = yf.Ticker('AMZN')
df = amazon.history(period='1d', interval='5m', actions=False)
data = df['Open'].to_numpy(dtype=float)

plt.plot(df['Open'])
plt.xticks([])
plt.show()