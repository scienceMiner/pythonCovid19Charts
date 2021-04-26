'''
Created on 3 Apr 2020
@author: ethancollopy
'''

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.ticker as ticker
import pylab as pl
import matplotlib.animation as animation
import logging

logging.basicConfig(level=logging.INFO)


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

Country1 = 'United Kingdom'
Country2 = 'Japan'

ax = fig.add_subplot(111, projection='3d')

ax.set_title( 'COVID-19 Cases & Deaths: %s vs %s' %(Country1, Country2)   )
ax.set_xlabel('Date')   
ax.set_ylabel('Number of Cases')
ax.set_zlabel('Deaths')
ax.set_facecolor('gainsboro')

        
def plot1(country, data, casesData):
    ukData1 = data[ ( data['Country/Region'] == country ) & (  data['Province/State'].isnull() ) ] 
    countryKey = ukData1.index[0]
    droppedData = ukData1.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    data5 = droppedData.transpose()
    singleCasesData = casesData[ ( casesData['Country/Region'] == country ) & (  casesData['Province/State'].isnull() ) ] 
    droppedCasesData = singleCasesData.drop(['Province/State','Country/Region','Lat','Long'], axis = 1) 
    data6 = droppedCasesData.transpose()
  
    N = len(data5.index.values)
    minVal = pl.datestr2num(datetime.strptime(data5.index.values[0], '%m/%d/%y' ).strftime('%m/%d/%y') )
                   
    print(data5.index.values[N-1])
    print(" minVal ", minVal )

    def format_date(x, pos=None):
        logging.debug("Input to format_date".format( int(x) )  )
        logging.debug(" Length of array {} ".format(N))

      #  print( "First  " , datetime.strptime(data5.index.values[0], '%m/%d/%y' ).strftime('%m/%d/%y') )
      #  print( "Last  ",  datetime.strptime(data5.index.values[N-1], '%m/%d/%y' ).strftime('%m/%d/%y')  )
      #  print( "First " , pl.datestr2num( datetime.strptime(data5.index.values[0], '%m/%d/%y' ).strftime('%m/%d/%y')  )  )
      #  print( "Last ",   pl.datestr2num( datetime.strptime(data5.index.values[N-1], '%m/%d/%y' ).strftime('%m/%d/%y')  )  )
       
        minVal2 = pl.datestr2num( datetime.strptime(data5.index.values[0], '%m/%d/%y' ).strftime('%m/%d/%y') ) 
        thisind = int(x-minVal2)
        
        if (thisind > N-1):
            thisind = N-1
        if (thisind < 0):
            thisind = 0
        logging.debug(" INDEX :  {} ".format(thisind))
       # strftime removes the time component  
        return datetime.strptime(data5.index.values[thisind], '%m/%d/%y' ).strftime('%m/%d/%y')#      return datetime.strptime(xV[thisind], '%m/%d/%y' ).strftime('%m/%d/%y')

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))

    for tl in ax.w_xaxis.get_ticklabels(): # re-create what autofmt_xdate but with w_xaxis
        tl.set_ha('right')
        tl.set_rotation(30)
        
    #ax.plot_trisurf(pd.to_datetime(data5.index.values, format='%m/%d/%y' ), data6[countryKey], data5[countryKey]  ) 
    plt = ax.plot_trisurf(pl.datestr2num(data5.index.values), data6[countryKey], data5[countryKey]  ) 
     
  
data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv") 
casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv") 


plot1(Country1, data, casesData )
plot1(Country2, data, casesData )

plt.savefig('charts/3D_uk_vs_france_jan2021.png')
plt.show()

