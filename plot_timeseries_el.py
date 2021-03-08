import sys
import numpy as np
import netCDF4 as nc
import pandas as pd
import geopandas
from pyschism.mesh import Hgrid,base
import matplotlib.pyplot as plt

sys.path.insert(0,"/Users/lcui/Packages/pylibs/Utility/")
from pylib import *

inode = 96629
#Read water level at inode
fn = '../examples_pyschism/staging/outputs/schout_0000_1.nc'
ds = nc.Dataset(fn)
#print(ds['elev'])
#Extract water elevation at node 96629 (index starts from 0)
el = ds['elev'][:,inode-1]
el = list(el)

#NOAA station: Chesapeake Channel, VA (CBBT, ID: 8638901)
#lon=-76.83,lat=37.03
df2 = pd.DataFrame({'Longitude':[-76.83],'Latitude':[37.03]})
plt.plot(el)
date = datenum(2021,3,4)
print(date)
plt.show()

