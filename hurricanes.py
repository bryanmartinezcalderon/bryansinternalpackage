# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import geopandas as gpd


def coordinatetoStr(arg):
    output = 0
    arg.lstrip()
    if 'N' in arg or 'E' in arg:
        output = int(arg[:3])
    elif 'S' in arg or 'W' in arg:
        print(arg)
        output = int(arg[:1])*-1
    return output


hurricanesfile = 'data/Hurricanes/Hurdat_Atlantic_Basin.csv'
shapefile = 'data/Hurricanes/ne_110m_ocean.shp'
columnnames2 = ['HurricaneID', 'HurricaneName', 'EntryNum']
columnnames = list(range(0, 21))

hurricaneCsv = pd.read_csv(hurricanesfile)
mapObject = gpd.read_file(shapefile)

# cleaning lists
hurrDataframe = pd.DataFrame(hurricaneCsv)
hurrDataframe.columns = columnnames
hurrList = hurrDataframe.loc[hurrDataframe[0].str.contains('A')]
hurrList = hurrList.drop(columns=list(range(3, 21)))
hurrList.columns = columnnames2
hurrDetails = hurrDataframe.loc[~hurrDataframe[0].str.contains('A')]

coordinates = hurrDetails.drop(columns=list(range(0, 4)))
coordinates = coordinates.drop(columns=list(range(6, 21)))

coordinates.applymap(coordinatetoStr)

mapObject.plot()
.plot()
