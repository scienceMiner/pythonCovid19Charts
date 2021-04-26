'''
Created on 15 Apr 2021

@author: ethancollopy
'''

import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
import country_converter as coco

cc = coco.CountryConverter()

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

some_names = ['United Rep. of Tanzania', 'Cape Verde', 'Burma',
              'Iran (Islamic Republic of)', 'Korea, Republic of',
              "Dem. People's Rep. of Korea"]

standard_names = cc.convert(names = some_names, to = 'ISO3')
UNmembership = cc.convert(names = some_names, to = 'UNmember')
print(standard_names)
print(UNmembership)
  
    

def geoplotForSingleDay( InputDate, data ):
    # data29 = data[data['Province/State'].isnull()] 
    data22 = data.groupby(['Country/Region']).sum()  # group over countries split by region or province
    #   print(data222['United Kingdom'])
    data222 = data22.transpose()  
    data3 = data222.diff()
    for col in data3.columns:
        data3.rename(columns={col:cc.convert(col, to='ISO3', not_found=None )}, inplace=True    ) 
    singleDayForCountries = data3.loc[InputDate]
    singleDayForCountries = pd.to_numeric(singleDayForCountries)
    fig = px.choropleth(singleDayForCountries,  locations=singleDayForCountries.index,
                    color=InputDate, 
                    hover_name=InputDate, # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma )
    titleText = "Daily Covid Deaths as of {}".format(InputDate)
    fig.update_layout(
    title={
        'text': titleText,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

    fig.show()
    
    
today = datetime.date.today()
print (today.strftime("%-m/%d/%y"))

#data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"  , index_col='Country/Region') 
data = pd.read_csv("/Users/ethancollopy/dev/git/data/COVID19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"  , index_col='Country/Region' ) 

geoplotForSingleDay( "4/24/21" ,  data )
    

