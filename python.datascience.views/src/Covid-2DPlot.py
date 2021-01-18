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

#fig = plt.figure();
#ax = fig.add_subplot(111, projection='3d')
    
def plot1(country, data, casesData):
#    print (data)
    ukData1 = data[ ( data['Country/Region'] == country ) & (  data['Province/State'].isnull() ) ] 
    countryKey = ukData1.index[0]
    print (data)
    droppedData = ukData1.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    print(droppedData)
    data5 = droppedData.transpose()
    print (data5)
    singleCasesData = casesData[ ( casesData['Country/Region'] == country ) & (  casesData['Province/State'].isnull() ) ] 
    droppedCasesData = singleCasesData.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    data6 = droppedCasesData.transpose()
    ax.plot_trisurf(pd.to_datetime(data5.index.values), data6[countryKey],data5[countryKey]) 
    
def plot2(country, data ):
    ukData15= data[ ( data['Country/Region'] == country ) & (  data['Province/State'].isnull() ) ] 
    droppedData = ukData15.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    print(droppedData)
    data51 = droppedData.transpose()
    print (data51)
    data51.plot()
    
    
def plot3( data ):
    country1 = 'Spain'
    country2 = 'Italy'
    ukData15= data[  (( data['Country/Region'] == country1)  or (data['Country/Region'] == country2) ) & (  data['Province/State'].isnull() ) ] 
    droppedData = ukData15.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    print(droppedData)
    data51 = droppedData.transpose()
    print (data51)
    data51.plot()
    
#mydateparser = lambda x: pd.datetime.strptime(x, "%d/%m/%Y")

#df = pd.read_csv("file.csv", sep='\t', names=['date_column', 'other_column'], parse_dates=['date_column'], date_parser=mydateparser)

data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"  , index_col='Country/Region' ) 
data22 = data[data['Province/State'].isnull()] 
data2 = data22.transpose()

for country in data2.columns: 
    print(country)
    
#print(data2)
Countries=['Germany','United Kingdom','Spain','Italy','India','Brazil','Russia','Japan','US']

data3= data2[Countries]
#data3 = data33.dropna(axis='columns')
#data4 = data3.loc[data3['Province/State'].isnull()] 
    
s4=data3.index.values

data4 = data3.iloc[34:,:]   
#data4=data3.loc['1/31/20':'1/31/25'])
#print(data4)

ax = data4.plot(lw=1, colormap='jet', marker='.', markersize=4,title='Covid-19 Deaths')#.set_xlabel('Date').set_ylabel('Number of Cases')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Deaths')
ax.set_facecolor('whitesmoke')

plt.grid()
plt.savefig('charts/covid19Deaths_jan21')
###print( data.loc['Spain':'Italy'] )

casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"  , index_col='Country/Region') 
casesData22 = casesData[data['Province/State'].isnull()] 
casesData2 = casesData22.transpose()
casesData3 = casesData2[Countries]
casesData4 = casesData3.iloc[34:,:]
# Adding moving average
#casesData4['pandas_SMA_3'] = casesData3.iloc[:,[0]].rolling(window=3).mean()

#print(casesData4)

casesData5= casesData3.iloc[:, 1:5]
casesData6= casesData5.diff()

print( ' CASES 3 to 5 ')

print(casesData6)

ax = casesData4.plot(lw=1, colormap='jet', marker='.', markersize=4,title='Covid-19 Cases')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Cases')
ax.set_facecolor('gainsboro')

plt.grid()
plt.savefig('charts/covid19Cases_jan21')
plt.show()




