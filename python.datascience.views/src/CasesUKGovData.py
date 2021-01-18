'''

Created on 4 Nov 2020
@author: ethancollopy

'''

import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

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
  
def barPlot():
    data = pd.read_csv("/Users/ethancollopy/Downloads/dataCases.csv"  , index_col='date' ) 
    #deathData6= data.diff()
    data=data.iloc[::-1]# casesData6.columns = ['Cases']
    mergedDF = pd.concat([data], axis=1 ) # axis 1 is for the same index 
    #newDF = mergedDF.drop(mergedDF.index[[1..40]])
    mergedDF = mergedDF.drop(mergedDF.index[0:40])
   # print('index to drop' + mergedDF.index[[1,40]])
    print(mergedDF)
    #ax = mergedDF.plot.bar(x='date',y='cumCasesByPublishDate')
    ax = mergedDF.plot.bar(y=['cumCasesByPublishDate','cumDeaths28DaysByDeathDate'])
    ax.set_title(" UK COVID-19 Cases & Deaths" )
    ax.set_xlabel('Date')   
    ax.set_ylabel('Number of Cases (m)')
    ax.set_facecolor('gainsboro')
    #ax.ticklabel_format(style='plain')
    ax.get_yaxis().set_major_formatter(tick.FuncFormatter(lambda x, p: format(int(x)/1000000, ','))) # stop format truncation
    
#    ax.ticklabel_format(useOffset=False)
 
    for i, t in enumerate(ax.get_xticklabels()):
        if (i % 10) != 0:
          t.set_visible(False)
           
    ax.xaxis.set_minor_locator(plt.MaxNLocator(40))

    return data


data1 = barPlot()

# plt.locator_params(nbins=40)
# plt.savefig('UKCases_Nov20.png')
plt.grid
plt.show()




