'''
Created on 26 Mar 2021

@author: ethancollopy
'''


import numpy as np
import matplotlib.pyplot as plt


def coin_toss_all_heads(num_coins, num_samples):
    " Toss coins and find probability they are heads"
    rng = np.random.default_rng()
    vals = rng.binomial(num_coins, 0.5, num_samples)
    fig = plt.hist(vals, density = True, bins=np.arange(-0.5, num_coins + 1.5, 0.5))
    print(f" approx {sum(vals == num_coins) / num_samples} " )
    print(f" expected : {0.5 ** num_coins } ")
    
coin_toss_all_heads(5, 100000)

plt.show()