'''
Created on 3 Apr 2020
@author: ethancollopy
'''

import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.rcParams.update({'font.serif': 'Times New Roman',
                                'font.size': 10.0,
                                'axes.labelsize': 'Medium',
                                'axes.labelweight': 'normal',
                                'axes.linewidth': 0.8,
                                 # THIS IS THE IMPORTANT ONE FOR STRETCHING
                                 # default is [6,4] but...i changed it to
                                'figure.figsize':[16,8]   # THIS ONE #
                              })

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d')
    
def plot1(country, data, casesData):
    ukData1 = data[ ( data['Country/Region'] == country ) & (  data['Province/State'].isnull() ) ] 
    countryKey = ukData1.index[0]
    droppedData = ukData1.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    data5 = droppedData.transpose()
    singleCasesData = casesData[ ( casesData['Country/Region'] == country ) & (  casesData['Province/State'].isnull() ) ] 
    droppedCasesData = singleCasesData.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    data6 = droppedCasesData.transpose()
    ax.plot_trisurf(pd.to_datetime(data5.index.values), data6[countryKey],data5[countryKey]) 
    

data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv") 
casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv") 

#plot1('Spain', data, casesData )
plot1('United Kingdom', data, casesData )
#plot1('Italy', data, casesData )
plot1('Germany', data, casesData)

#Add column name to plot 
plt.show()

