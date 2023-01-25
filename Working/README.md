## Algorithms
1. Moving Average (*movingAverage.py*)
   
   * Measures the moving average of a given stock with a given period and an interval.
   The algorithm buys the share if it is above the average and sells if it is below the running average.  
   
   Usage:
   ```
   python movingAverage.py
   ```
   
   Output:  
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/movingAverage.gif)  
   
   Problems:
   * We miss out selling before downard trends and buying at the beginning of upward trends.
   Thus, we end up incurring great losses.
   * We need a way to follow the trends.
   
2. BOLL Bands Visualization (*bollBands.py*)
   
   * Displays upper and lower BOLL bands alongwith the average and the shaded area in between.  
   
   Usage:
   ```
   python bollBands.py
   ```
   
   Output:   
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/BOLLBands.png) 
   
3. Follow Trends (*followTrend.py*)
   
   * Follows the moving average of a given stock with a given period and an interval.
   The algorithm buys the share if the average trend is increasing and sells if the average is decreasing.  
   * We sell immediately if the average decreases (and the selling price is higher than the buying price)
   because for the average to decrease rapidly the price must have changed drastically.
   * We cannot sell if the price is lower than the buying price because it leads to the same issues as before
   i.e. we end up selling at immensely low prices.
   * However, the result of this algorithm is a significant improvement because we take advantage out of big trends.
   
   Usage:
   ```
   python followTrend.py
   ```
   
   Output:  
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/FollowTrends.png)  
   
   Problems:
   * The main problem is that we might miss out on some trends because we cannot sell at a lower price than the
   buying price.
   * For example, at the end of the above graph, we miss out on the last drastic price increase.
   * One possible solution is to implement partial buying (separate buy prices to follow multiple trends).
     
4. Follow Partial Trends (*followPartialTrend.py*)
   
   * An attempt to solve the issues discovered in the *Follow Trends* algorithm.
   * Here we split the investment into separate parts. In doing so, we are able to buy on most trends by splitting our
   investment over time instead of investing it all at once.
   * Selling is similar to the previous algoirthm i.e. we sell immediately if the average decreases (and the selling price is higher than the buying price)
   because for the average to decrease rapidly the price must have changed drastically.
   * Thus, more splits correlate with less chances of missing out as we can see in the figures below.
   
   Usage:
   ```
   python followPartialTrend.py
   ```
   
   Output:  
   *10 splits*  
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/FollowPartialTrends10.png)  
   *50 splits*  
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/FollowPartialTrends50.png)  
   *100 splits*  
   ![alt text](https://github.com/rp247/Naive-Trade/blob/main/Working/Demos/FollowPartialTrends100.png)  
   
   Problems:
   * The results of this "improved" algorithm are worse than that of the previous one primarily because
   we have low investments at every split(s) and we trade too heavily (for short profits).
   
## Files
1. dataCollector.py&emsp;&emsp;&emsp;&ensp;:&emsp;Collects data of a given *ticker* within an *interval* and *period*. 
2. discountedAverage.py&emsp;:&emsp;Calculates the moving average given an *alpha* (*alpha* ∝ accuracy of average). 
3. grapher.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;:&emsp;Graphs the results (*prices*, *sells*, *averages*, etc.).
4. movingAverage.py&emsp;&emsp;&ensp;:&emsp;Implementation of the *Moving Average* algorithm.
5. bollBands.py&emsp;&emsp;&emsp;&emsp;&emsp;:&emsp;Visualization of BOLL bands.
6. followTrend.py&emsp;&emsp;&emsp;&emsp;&nbsp;:&emsp;Buy on increasing average trends, sell on decreasing averages.
7. followPartialTrends&emsp;&emsp;&ensp;:&emsp;An attempt to buy on most of the increasing average trends, sell on decreasing averages.
