'''
Created on 6 July 2020
@author: ethancollopy

'''

import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.dates as mdates
import datetime as DT
import time

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

data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"  , index_col='Country/Region' ) 
data22 = data[data['Province/State'].isnull()] 
droppedData = data22.drop(['Province/State','Lat','Long'], axis = 1) 
transposedData = droppedData.transpose()


def plot(cx , data, Country, daysToSkip):
    Countries=[ Country ]
    data3 = data[Countries]
    s4 = data3.index.values
    data4 = data3.iloc[daysToSkip:,:]   
    countryKey = data4[ Country ]
    y = countryKey
    y2 = np.array(y)
    x = mdates.datestr2num(data4.index.values)
    x2 = np.array(x)
    z4 = np.polyfit(x2, y2, 3)
    p4 = np.poly1d(z4)
    xx_out = np.linspace(x2.min(), x2.max()+60, 300)
    #y3 = np.polyval(z4,x2) 
    legend = "{} Deaths to date".format(Country)
    legendExtrapolated = "{} Deaths Naive Projection".format(Country)
    dd_out = mdates.num2date(xx_out) # CONVERT BACK TO DATES 
    cx.plot(dd_out, p4(xx_out),'-g', label=legendExtrapolated) # PLOT EXTRAPOLATED VALUES    
    cx.plot(x2, y2, '+', label=legend)  #  PLOT ORIGINAL VALUES 
    cx.grid()
    
fig, cx = plt.subplots()
cx.grid()
cx.legend()
cx.set_xlabel('Date')
cx.set_ylabel('Number of Deaths')
cx.set_title('Number of Deaths - Naive Extrapolation')
cx.set_facecolor('gainsboro')

daysToSkip=48
plot(cx, transposedData, 'India', daysToSkip )
plot(cx, transposedData, 'Brazil', daysToSkip )
plot(cx, transposedData, 'US', daysToSkip )
# for country in data2.columns: 
#    print(country)
plt.legend(loc="upper left")
plt.grid()

plt.savefig('Covid19_NaiveDeathExtrap_Aug20.png')









