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
    
    
#mydateparser = lambda x: pd.datetime.strptime(x, "%d/%m/%Y")

#df = pd.read_csv("file.csv", sep='\t', names=['date_column', 'other_column'], parse_dates=['date_column'], date_parser=mydateparser)

data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"  , index_col='Country/Region' ) 
data22 = data[data['Province/State'].isnull()] 
data2 = data22.transpose()
Countries=['Germany','United Kingdom','Spain','Italy','India','Brazil','Russia','Japan','Sweden']
data3= data2[Countries]
deathData4 = data3.iloc[54:,:]   
deathData5= data3.iloc[34:, 1:2]
deathData6= deathData5.diff()

###print( data.loc['Spain':'Italy'] )

casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"  , index_col='Country/Region') 
casesData22 = casesData[data['Province/State'].isnull()] 
casesData2 = casesData22.transpose()
casesData3 = casesData2[Countries]
casesData4 = casesData3.iloc[54:,:]
casesData5= casesData3.iloc[34:, 1:2]   # so just having 2 and not 2:3 loses the columnt title 
casesData6= casesData5.diff()



casesData6=casesData6.iloc[1:] #remove the first row 
deathData6=deathData6.iloc[1:]

print( ' DEATHS 3 to 5 ')
casesData6.rename(columns=casesData6.iloc[0])

deathData6.columns = ['Deaths']
casesData6.columns = ['Cases']
print(casesData6)


cols = [0]
#deathData6 = deathData6[deathData6.columns[cols]]
#casesData6 = casesData6[deathData6.columns[cols]]

#deathData6 = deathData6[["Spain"]]
#casesData6 = casesData6[['Spain']]


deathRow_Count = deathData6.size
print (deathRow_Count )

casesRow_Count = casesData6.size
print (casesRow_Count )


#x = range(row_Count)
#The below code will create two plots. The parameters that .subplot take are (row, column, no. of plots).
#plt.subplot(299)
#This will create the bar graph for poulation

#  mergedDF = pd.merge(casesData6, deathData6 , how="outer" )

mergedDF = pd.concat([casesData6,deathData6], axis=1 )
#df.set_index('Country/Region', inplace=True)

print(mergedDF)
ax = mergedDF.plot.bar()


ax.set_title(" United Kingdom COVID-19 Cases & Deaths")
ax.set_xlabel('Date')   
ax.set_ylabel('Number of Cases')
ax.set_facecolor('gainsboro')



for i, t in enumerate(ax.get_xticklabels()):
    if (i % 5) != 0:
        t.set_visible(False)

#                                    plt.xticks(x, casesData6.index, rotation='vertical')

plt.grid
plt.show()



