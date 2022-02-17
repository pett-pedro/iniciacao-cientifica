from pygsp import graphs, plotting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plotting.BACKEND = 'matplotlib'

### Dataframe with only the latitude and longitude informations
df = pd.read_csv("C:\\Users\\pette\\Desktop\\petinho\\uacsa\\Iniciação Científica\\meus programas\\script_csv_temp\\dados_lat_long_alt_temp ATUALIZADO.csv",
                 usecols=[0,1])

###Latitude and longitude data columns
latitude = df.iloc[0:, 0:1]
longitude = df.iloc[0:, 1:2]

###Dataframe to numpy array
latitude = latitude.to_numpy()
longitude = longitude.to_numpy()
df = df.to_numpy()

###Set the coordinate system as: longitude = x axis and latitude = y axis
x, y = longitude, latitude
coords = np.stack([x, y], axis=1)

###Generating a nearest-neighbor graph from point cloud
G = graphs.NNGraph(df, k= 10, center= True, rescale= True)

###Plot coordinates and plot
G.set_coordinates(kind= coords)
G.plot()
plt.show()
