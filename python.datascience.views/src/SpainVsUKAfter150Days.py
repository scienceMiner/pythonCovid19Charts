'''

Created on 4 May 2020
@author: ethancollopy

'''

import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

plt.rcParams.update({'font.serif': 'Times New Roman',
                                'font.size': 10.0,
                                'axes.labelsize': 'Medium',
                                'axes.labelweight': 'normal',
                                'axes.linewidth': 0.8,
                                 # THIS IS THE IMPORTANT ONE FOR STRETCHING
                                 # default is [6,4] but...i changed it to
                                'figure.figsize':[16,8]   # THIS ONE #
                              })

  
#print(data2)
Countries=['Spain','United Kingdom']


casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"  , index_col='Country/Region') 
casesData22 = casesData[casesData['Province/State'].isnull()] 
casesData2 = casesData22.transpose()
casesData3 = casesData2[Countries]
casesData4 = casesData3.iloc[150:,:]

# Adding moving average
#casesData4['pandas_SMA_3'] = casesData3.iloc[:,[0]].rolling(window=3).mean()

casesData5= casesData3.iloc[:, 1:5]
casesData6= casesData5.diff()

ax = casesData4.plot(lw=1, colormap='jet', marker='.', markersize=4,title='Covid-19 Cases')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Cases')
ax.set_facecolor('gainsboro')


plt.grid()
plt.show()




