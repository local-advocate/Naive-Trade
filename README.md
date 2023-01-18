# Description

An approach to make trading algorithms. 

These are beginner approaches to understand the issues of algorithmic trading and to understand more advanced algorithms better.  

The algorithms also show statistics (total profit, etc.) and graphs (share prices, when the algorithm traded, etc.)

## Files & Folders

1. Experiment  
   1. simpleAlgo.py&emsp;&emsp;:&emsp;Buy on upwards trend and sell on a downwards trend.  
   2. yFinance.py&emsp;&emsp;&emsp;:&emsp;*simpleAlgo.py* combined with real world data using the *yfinance* library.
   3. average.py&emsp;&emsp;&emsp;&nbsp;:&emsp;Takes average of every running data point. Buys when below average, sells when above it.
   3. discAvgrator.py&emsp;&nbsp;:&emsp;Take running + discounted averages efficiently.
   4. discAverage.py&emsp;&ensp;:&emsp;Same idea as *average.py* but with a much accurate average (only the last few points matter).
   4. deviation.py&emsp;&ensp;&emsp;&nbsp;:&emsp;Sell when stock prices start deviating back to average and viceversa.
   5. README.md&emsp;&emsp;&ensp;:&emsp;Explanation of the algorithms and problems with them.
   6. images&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;:&emsp;Folder consisting images regarding the algorithm results.

## How to Run

* Libraries Required

   1. numpy  
   2. matplotlib
   3. yfinance
   
* Program Instructions

   Each file can be run individually. See the descriptions and comments inside the files for functionality.

## References
