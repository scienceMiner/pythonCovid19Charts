'''
Created on 9 Jul 2020

@author: ethancollopy
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as dates
import datetime, random
import matplotlib.ticker as ticker

def random_date():
    date = datetime.date(2008, 12, 1)
    while 1:
        date += datetime.timedelta(days=30)
        yield (date)

def format_date(x, pos=None):
    return dates.num2date(x).strftime('%Y-%m-%d') #use FuncFormatter to format dates

r_d = random_date()
some_dates = [dates.date2num(next(r_d)) for i in range(0,20)]

print(format_date(random_date()))

print(some_dates)
