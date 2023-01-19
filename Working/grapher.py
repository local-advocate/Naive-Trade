import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, data=[], average=[], deviation=[], sell=[], buy=[]):
        self.average = average
        self.deviation = deviation
        self.sell = sell
        self.buy = buy
        self.data = data

    def graphit(self):
        if len(self.data) != 0: plt.plot(self.data, color='b')                                    # plot data
        else: return
        if len(self.average) != 0: plt.plot(self.average, color='m', ls='dashed')                 # plot average
        if len(self.deviation) != 0: plt.plot(self.deviation, color='y', ls='dashed')             # plot average
        if len(self.sell) != 0:                                                                   # plot sell
            for xc in self.sell:
                plt.plot(xc, self.data[xc], 'ro', markersize=2)
        if len(self.buy) != 0:                                                                    # plot buy
            for xc in self.buy:
                plt.plot(xc, self.data[xc], 'go', markersize=2)
        plt.show()
