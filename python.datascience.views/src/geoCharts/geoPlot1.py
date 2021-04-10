'''
Created on 30 Jan 2021
@author: ethancollopy
'''

import pandas as pd
#    import plotly.graph_objs as go 
import plotly.express as px
import json

from plotly.offline import init_notebook_mode,iplot, plot

#init_notebook_mode(connected=True)

with open('/Users/ethancollopy/git/pythonPlotting/python.datascience.views/src/data/countries.geojson', 'r') as myfile:
    data=myfile.read()

# parse file
countries = json.loads(data)

df = pd.read_csv('/Users/ethancollopy/git/pythonPlotting/python.datascience.views/src/data/2014_World_Power_Consumption_Data')
df.info()

print(df)
#data = dict(
#      type = 'choropleth',
#     colorscale = 'Viridis',
#    locations = df['Country'],  
#   locationmode = 'country names',
#   z = df['Power Consumption KWH'],
#   text = df['Country'],
#   colorbar = {'title' : 'Power Consumption KWH'}
# )

#layout = dict(title = '2014 Power Consumption KWH',   
#                       geo = dict(projection = {'type':'mercator'})
#           )

#choromap = go.Figure( data = [data], layout = layout )
#iplot(choromap, validate=False)


fig = px.choropleth(df, geojson=countries, locations='Country', color='Power Consumption KWH',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="world",
                           labels={'Power Consumption KWH':'Power Consumption KWH'}
                          )
fig.update_geos(projection_type="mercator")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


