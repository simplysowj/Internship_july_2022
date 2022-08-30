from asyncio.windows_events import NULL
from ftplib import all_errors
from pickletools import long1
import streamlit as st
st.title("Nearest pubs based on lattitude and longitude")

import numpy as np
import pandas as pd
import sklearn.neighbors

import plotly.express as px
import plotly.graph_objects as go

from sklearn.neighbors import BallTree, KDTree
df=pd.read_csv("pubs.csv")
check="N"
df['latitude'] =  pd.to_numeric(df['latitude'],errors='coerce')

df['longitude'] = pd.to_numeric(df['longitude'],errors='coerce')

df[['lat_radians_X','long_radians_X']] = (
    np.radians(df.loc[:,['latitude','longitude']])
)
lat1=st.number_input('lat')
lon1=st.number_input('lon')
print(lat1)
print(lon1)
df_copy = pd.DataFrame(index=df.index,columns=df.columns)
df_copy =df.loc[(df['latitude'] == lat1) & (df['longitude'] == lon1)]
indices=""
distances=""
import numpy as np
from sklearn.neighbors import BallTree

tree = BallTree(df[['lat_radians_X','long_radians_X']], leaf_size=2)  

try: 
          
    distances, indices = tree.query(df_copy[['lat_radians_X','long_radians_X']], k=5)  

except (ValueError,NameError):

    st.error('Please enter the values')




to_concat = []
for i, m in enumerate(indices):
    
    loc = df.iloc[i, :]['latitude']  # str of location of interest's name
    neighbors = df.iloc[m, :]['longitude']  # pd.Series of n+1 nearest neighbors' names
  
    if loc in neighbors.values:
        
        mask = (neighbors != loc)
        neighbors = neighbors[mask]
               
    else:
        neighbors = neighbors[:-1]
                

            # df for visibility into distances and index in market list
    for _, neighbor in enumerate(neighbors):
         to_concat.append([loc, neighbor])

df_new = pd.DataFrame(to_concat, columns=['latitude',
                                              "longitude"
                                              
                                              ])

loc_map = df_new.groupby("latitude").agg({"longitude": lambda x: list(x)})['longitude'].to_dict()

st.write("Here's the neighboring pub names : ")

st.write(loc_map)
st.map(df_new)

to_concat = []
for i, m in enumerate(indices):
    
    loc = df.iloc[i, :]['name']  # str of location of interest's name
    neighbors = df.iloc[m, :]['name']  # pd.Series of n+1 nearest neighbors' names
  
    if loc in neighbors.values:
        
        mask = (neighbors != loc)
        neighbors = neighbors[mask]
               
    else:
        neighbors = neighbors[:-1]
                

            # df for visibility into distances and index in market list
    for _, neighbor in enumerate(neighbors):
         to_concat.append([loc, neighbor])

df_new = pd.DataFrame(to_concat, columns=['location',
                                              "neighbor"
                                              
                                              ])

loc_map = df_new.groupby("location").agg({"neighbor": lambda x: list(x)})['neighbor'].to_dict()

st.write("Here's the neighboring pub names : ")

st.write(loc_map)
st.write(df_new)
