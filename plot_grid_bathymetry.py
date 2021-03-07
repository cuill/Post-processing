import sys
import numpy as np
import netCDF4 as nc
import pandas as pd
import geopandas
from pyschism.mesh import Hgrid,base
import matplotlib.pyplot as plt

sys.path.insert(0,"/Users/lcui/Packages/pylibs/Utility/")
from pylib import *

#Load hgrid file
inode = 2348
gd = read_schism_hgrid('../../../Gulf_Stream_develop/hgrid.gr3')
lon = list(gd.x)
lat = list(gd.y)
print(np.max(lon))
print(np.min(lon))
print(np.max(lat))
print(np.min(lat))
df = pd.DataFrame({'Longitude':lon, 'Latitude':lat})
print(df.head())

#Plot 
figure(figsize=[16,6])
subplot(1,3,1)
gd.plot_grid(plotz=1,ec=None,clim=[0,50],ticks=linspace(0,50,11))
setp(gca(),xticks=[],yticks=[])
set_cmap('jet')

subplot(1,3,2)
gd.plot_grid(); gd.plot_bnd(c='b',lw=0.5)
setp(gca(),xticks=[],yticks=[])
setp(gca(),xticks=[],yticks=[])

subplot(1,3,3)
gd.plot_bnd(c='rg',lw=2)
setp(gca(),xticks=[],yticks=[])

gcf().tight_layout()
#Read water level at inode
fn = './schout_0000_1.nc'
ds = nc.Dataset(fn)
#print(ds['elev'])
el = ds['elev'][191,:]
el = list(el)


gcf().tight_layout()


#NOAA station: Chesapeake Channel, VA (CBBT, ID: 8638901)
#lon=-76.83,lat=37.03
df2 = pd.DataFrame({'Longitude':[-76.83],'Latitude':[37.03]})
#plt.plot(el)
plt.show()

