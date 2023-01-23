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
   
## Files
1. dataCollector.py&emsp;&emsp;&emsp;&ensp;:&emsp;Collects data of a given *ticker* within an *interval* and *period*. 
2. discountedAverage.py&emsp;:&emsp;Calculates the moving average given an *alpha* (*alpha* ∝ accuracy of average). 
3. grapher.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;:&emsp;Graphs the results (*prices*, *sells*, *averages*, etc.).
4. movingAverage.py&emsp;&emsp;&ensp;:&emsp;Implementation of the *Moving Average* algorithm.
5. bollBands.py&emsp;&emsp;&emsp;&emsp;&emsp;:&emsp;Visualization of BOLL bands.
