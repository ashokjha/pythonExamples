# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:11:32 2021

@author: Ashok Kumar Jha
"""

'''
In lesson we will learn about Monte Carlo Simulation. 
First an introduction to the concept and then how to use Sharpe Ratio 
to find the optimal portfolio with Monte Carlo Simulation.

Learning objectives
1. The principles behind Monte Carlo Simulation
2. Applying Monte Carlo Simulation using Sharpe Ratio to get the optimal portfolio
3. Create a visual Efficient Frontier based on Sharpe Ratio

Monte Carlo Simulation is a great tool to master. It can be used to simulate 
risk and uncertainty that can affect the outcome of different decision options.

Simply said, if there are too many variables affecting the outcome, then it 
can simulate them and find the optimal based on the values.

Here we will first use it for simple example, which we can precisely calculate.
This is only to get an idea of what Monte Carlo Simulations can do for us.

The game we play.

You roll two dice.
When you roll 7, then you gain 5 dollars.
If you roll anything else than 7, you lose 1 dollar.
How can we simulate this game?

Well, the roll of two dice can be simulated with NumPy as follows.
'''
import numpy as np

def roll_dice():
    return np.sum(np.random.randint(1, 7, 2))

'''
Where are roll is simulated with a call to the roll_dice(). It simply uses the
np.random.randint(1, 7, 2), which returns an array of length 2 with 2 integers
in the range 1 to 7 (where 7 is not included, but 1 is). The np.sum(…) sums 
the two integers into the sum of the two simulated dice.

Now to the Monte Carlo Simulation.

This is simply to make a trial run and then see if it is a good game or not.
'''

def monte_carlo_simulation(runs=1000):
    results = np.zeros(2)
    for _ in range(runs):
        if roll_dice() == 7:
            results[0] += 1
        else:
            results[1] += 1
    return results

'''
This is done by keeping track of the how many games I win and lose.

A run could look like this.
'''
mcs=monte_carlo_simulation()
print(mcs)

'''
It could return array([176., 824.]), which would result in 
my win of 176*5 = 880 USD and lose of 824 USD. A total gain of 56 USD.

Each run will most likely give different conclusions.

A way to get a more precise picture is to make more runs. Here, 
we will try to record a series of runs and visualize them.
'''
results = np.zeros(1000)

for i in range(1000):
    results[i] = monte_carlo_simulation()[0]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.hist(results, bins=15)

'''
This gives an idea of how a game of 1000 rolls returns and how volatile it is. 
See, if the game was less volatile, it would center around one place.

For these particular runs we have that results.mean()*5 gives the average 
return of 833.34 USD (notice, you will not get the exact same number due to 
                      the randomness involved).

The average loss will be 1000 – results.mean() = 833.332 USD.

This looks like a pretty even game.

Can we calculate this exactly?

Yes. The reason is, that this is a simple situation are simulating. When we 
have more variable (as we will have in a moment with portfolio simulation) 
it will not be the case.

A nice way to visualize it is as follows.
'''
d1 = np.arange(1, 7)
d2 = np.arange(1, 7)
mat = np.add.outer(d1, d2)

print(mat)

#The exact probability for rolling 7 is.
print(mat[mat == 7].size/mat.size)
'''
Where we count how many occurrences of 7 divided by the number of 
possibilities. This gives 0.16666666666666667 or 1/5.

Hence, it seems to be a fair game with no advantage. This is the same we 
concluded with the Monte Carlo Simulation.

Now we have some understanding of Monte Carlo Simulation, we are ready to 
use it for portfolio optimization.

To do that, we need to read some time series of historic stock prices.
'''

import pandas_datareader as pdr
import datetime as dt


tickers = ['AAPL', 'MSFT','TWTR','IBM']
start = dt.datetime(2020, 1, 1)

data = pdr.data.get_data_yahoo(tickers, start)
data = data['Adj Close']
print(data)

#To use it with Sharpe Ratio, we will calculate the log returns.
log_returns = np.log(data/data.shift())

#The Monte Carlo Simulations can be done as follows.

# Monte Carlo Simulation
n = 5000

weights = np.zeros((n, 4))
exp_rtns = np.zeros(n)
exp_vols = np.zeros(n)
sharpe_ratios = np.zeros(n)

for i in range(n):
    weight = np.random.random(4)
    weight /= weight.sum()
    weights[i] = weight
    
    exp_rtns[i] = np.sum(log_returns.mean()*weight)*252
    exp_vols[i] = np.sqrt(np.dot(weight.T, 
                                 np.dot(log_returns.cov()*252, weight)))
    sharpe_ratios[i] = exp_rtns[i] / exp_vols[i]


'''
The code will run 5000 experiments. We will keep all the data from each run. 
The weights of the portfolios (weights), the expected return (exp_rtns), 
the expected volatility (exp_vols) and the Sharpe Ratio (sharpe_ratios).

Then we iterate over the range.

First we create a random portfolio in weight (notice it will have the sum 1). 
Then we calculate the expected annual return. The expected volatility is 
calculated a bit different than we learned in the lesson about Sharpe Ratio. 
This is only to make it perform faster.

Finally, the Sharpe Ratio is calculated.

In this specific run (you might get different values) we get that the maximum 
Sharpe Ratio is, given by sharpe_ratios.max(), 1.1398396630767385.

To get the optimal weight (portfolio), call weights[sharpe_ratios.argmax()]. 
In this specific run, array([4.57478167e-01, 6.75247425e-02, 4.74612301e-01, 
                             3.84789577e-04]). 
This concludes to hold 45.7% to AAPL, 6.7% to MSFT, 47.5% to TWTR, 
and 0,03% to IBM is optimal.

This can be visualized as follows in an Efficient Frontier.
'''




#Resulting in this chart.
# fig1, ax1 = plt.subplots()
# ax1.scatter(exp_vols, exp_rtns, c=sharpe_ratios)
# ax1.scatter(exp_vols[sharpe_ratios.argmax()], exp_rtns[sharpe_ratios.argmax()], c='r')
# ax1.set_xlabel('Expected Volatility')
# ax1.set_ylabel('Expected Return')


