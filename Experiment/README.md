## ***THIS IS FOR PESONAL USE ONLY. PLEASE SEE THE 'WORKING' DIRECTORY FOR BETTER DETAILS!***

# Algorithms
### 1. simpleAlgo.py/yFinance.py

* Explaination

   If the current price is less than the previous stock price (a decreasing trend), then sell the shares.
   If the current price is more than the previous price, hold it (an increasing trend).  
   
   The idea is that, as new data comes in, if we see a dowards trend we would sell the stock.
   And if we see an upwards trend, we hold onto it.
   
* Problems

   The problem is that when the new data points come in, we sell at a lower price quite often.
   This leads to high losses no matter how frequently we get the data.  
   
   Thus, we end up buying at the peaks and selling at much lower prices.
   If we say only sell if the price is higher than buying price, then most likely we will not be able to trade frequently.
   Matter of fact, we would make less than ten(s) trades.
   
   For example, here:  
   
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Experiment/images/simpleAlgoBad.png?raw=true)  
   
   The red lines are when we sell and the green lines are the prices we buy at. As we can see, we incur great loses.
   
### 2. average.py/discountAverage.py

* Explaination

   The idea here is to solve the problems of the *simpleAlgo.py* by taking a running average of the data.
   We buy if the price is less than average and sell if the price is above average.  
   
   *average.py* takes into account the average of the whole sequence while *discountAverage.py* only considers latest datapoints.
   The lower the value of alpha, the better the running average.
   
* Problems

   The problem with *average.py* is that it does not provide accurate average (it does not forget the past data).
   Thus, we again do not trade as much. It might work OK if the prices are consistent. However, that is quite rare.
    
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Experiment/images/averageBad.png?raw=true)  
   
   We only make few beneficial trade at the beginning only to incur losses when the price never comes back up.
   
   The problem with *discountAverage* is the same as *simpleAlgo*.
   We have a much better average but we still end up buying on higher prices and sell at lower ones due to the nature of our algorithm.
   
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Experiment/images/discountAvgBad.png?raw=true)
   
   We also miss out on high upward trends and spikes.
   
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Experiment/images/discUpwardMiss.png?raw=true)
   
   Here we prematurely sold at 51 (missing out the spike at 60).
   
   Likewise, we also miss out on not following downwards trends.
   
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Experiment/images/discDownwardMiss.png?raw=true)
   
   We could have sold way before the price got above average but significantly less than the buying price.
   
# Files
1. simpleAlgo.py&emsp;&emsp;:&emsp;Buy on upwards trend and sell on a downwards trend.  
2. yFinance.py&emsp;&emsp;&emsp;:&emsp;*simpleAlgo.py* combined with real world data using the *yfinance* library.
3. average.py&emsp;&emsp;&emsp;&nbsp;:&emsp;Takes average of every running data point. Buys when below average, sells when above it.
3. discAvgrator.py&emsp;&nbsp;:&emsp;Take running + discounted averages efficiently.
4. discAverage.py&emsp;&ensp;:&emsp;Same idea as *average.py* but with a much accurate average (only the last few points matter).
4. deviation.py&emsp;&ensp;&emsp;&nbsp;:&emsp;Sell when stock prices start deviating back to average and viceversa.
5. README.md&emsp;&emsp;&ensp;:&emsp;Explanation of the algorithms and problems with them.
6. images&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;:&emsp;Folder consisting images regarding the algorithm results.
   
   
