'''

Created on 4 May 2020
@author: ethancollopy

'''

import pandas as pd 
import matplotlib.pyplot as plt
import datetime

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
  
def barPlot(Country):
    data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"  , index_col='Country/Region' ) 
    data22 = data[data['Province/State'].isnull()] 
    data2 = data22.transpose()
    Countries=[Country]
    data3= data2[Countries]
    deathData5= data3.iloc[34:, 0:1]
    deathData6= deathData5.diff()
    casesData = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"  , index_col='Country/Region') 
    casesData22 = casesData[data['Province/State'].isnull()] 
    casesData2 = casesData22.transpose()
    casesData3 = casesData2[Countries]
    casesData5= casesData3.iloc[34:, 0:1]   # so just having 2 and not 2:3 loses the columnt title 
    casesData6= casesData5.diff()
    casesData6=casesData6.iloc[1:] #remove the first row 
    deathData6=deathData6.iloc[1:]
    deathData6.columns = ['Deaths']
    casesData6.columns = ['Cases']
    mergedDF = pd.concat([casesData6,deathData6], axis=1 ) # axis 1 is for the same index 
    ax = mergedDF.plot.bar()
    ax.set_title(" %s COVID-19 Cases & Deaths" %Country)
    ax.set_xlabel('Date')   
    ax.set_ylabel('Number of Cases')
    ax.set_facecolor('gainsboro')
    for i, t in enumerate(ax.get_xticklabels()):
        if (i % 5) != 0:
            t.set_visible(False)


today = datetime.date.today()
#                                    plt.xticks(x, casesData6.index, rotation='vertical')
barPlot("Italy")
plt.savefig("charts/ItalyCases_%s.png" % today  )
    
barPlot("India")
plt.savefig("charts/IndiaCases_%s.png" % today  )

barPlot("United Kingdom")
plt.savefig("charts/UKCases_%s.png" % today  )

barPlot("Croatia")
plt.savefig("charts/CroatiaCases_%s.png" % today  )

plt.grid
plt.show()




