'''
Created on 8 Jan 2021
@author: ethancollopy
'''

import requests
import csv
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

import datetime

def display(output_array):
    for line in output_array :
        print (" output: %s " % ( line ))
 
def saveResponseData(fileName, response ):
    write_file = (targetfile)
    with open(write_file, 'w') as f:
        writer = csv.writer(f, delimiter=' ', lineterminator='\n')
        writer.writerows(response.text.splitlines())
 
def removeQuotesFromArrayItems(input_array):       
    output_array = []
    print(input_array)
    for line in input_array :
        itemLine = line.split(",")
        #size = len(line.split(","))
        output_item = []
        for item in itemLine:
            output_item.append( item.replace('"','') )
        output_array.append(output_item)    

    return output_array

def getResponse(regionCode):
    query = {'areaType':'region', 'areaCode':regionCode,'metric':'cumDeaths28DaysByDeathDate','format':'csv'}
    response = requests.get('https://api.coronavirus.data.gov.uk/v2/data', params=query)
    return response


def populateDataframe( response ):
    output_array = removeQuotesFromArrayItems(response.text.splitlines())
    npArray = np.array(output_array)
    # Delete the date column at index 1 which we will use for an index 
    npArray2 = np.delete(npArray, 0, axis=1)
#print(npArray[:,[0]])    # index column
#print( npArray[[0], 1:5] ) # header row 
    newDataFrame = pd.DataFrame( npArray2,   # values
             index=npArray[:,[0]],    # 1st column as index
             columns= ['areaType','areaCode','areaName','cumDeaths28DaysByDeathDate'] )
    newDataFrame.index = newDataFrame.index.map("".join)
    newDataFrame = newDataFrame.drop(['date'])
    newRegionTitle = "Deaths" + str(newDataFrame['areaName'][0]).replace(" ","")
    newDataFrame = newDataFrame.drop(columns=['areaType','areaCode','areaName'])
    newDataFrame[["cumDeaths28DaysByDeathDate" ]] = newDataFrame[["cumDeaths28DaysByDeathDate" ]].apply(pd.to_numeric)
    newDataFrame['diff'] = newDataFrame['cumDeaths28DaysByDeathDate'].diff(-1)
    newDataFrame = newDataFrame.drop(columns=['cumDeaths28DaysByDeathDate'])
    newDataFrame = newDataFrame.rename(columns={ "diff": newRegionTitle })

    return newDataFrame

def formatPlot(ax,date):
    ax.set_title(" UK COVID-19 Daily Deaths by Region as of %s" % date)
    ax.set_xlabel('Date')   
    ax.set_ylabel('Number of Deaths')
    ax.grid(True)
    ax.set_facecolor('gainsboro')
    ax.tick_params(labelsize=8)
    
           
today = datetime.date.today()
print(today)

regions = [ ("london","E12000007"), ("southwest","E12000009"), ("eastmidlands","E12000004") , 
("NorthWest" , "E12000002" ) , ("YorksHum" , "E12000003" ) , ( "SouthEast" , "E12000008"  ) , 
("NorthEast" , "E12000001" ) , ("EastOfEngland" , "E12000006"  ) , ("WestMidlands" , "E12000005" ) ]

dataframeRegion_Dict = {} 

for region in regions:
    response = getResponse(region[1])
    df = populateDataframe(response)
    dataframeRegion_Dict[region[0]] = df
    targetfile = "/Users/ethancollopy/git/pythonPlotting/python.datascience.views/src/data/{}Data.csv".format(region[0])   
#    saveResponseData(targetfile, response)
    
print(dataframeRegion_Dict.keys())

finalDataframe = pd.DataFrame()

for region in regions:
    outputDf = dataframeRegion_Dict[region[0]]
    finalDataframe = pd.merge(finalDataframe, outputDf, left_index=True, right_index=True, how='outer')

ax = finalDataframe.plot(linewidth = "0.8")
formatPlot( ax, today )

print(finalDataframe)
 
plt.savefig("charts/UKDeaths_%s.png" % today )
plt.show()

                                                                                     
        
    
