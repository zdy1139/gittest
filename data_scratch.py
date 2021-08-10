import xarray as xr
import numpy as np
import pandas
import math
import os
from scipy.interpolate import griddata

# 读取历史数据
history_data = xr.open_dataset('DL_CORRECTION/ACCESS-CM2/histrical/siconc_SImon_ACCESS-CM2_historical_r1i1p1f1_gn_185001-201412.nc')
print(history_data)


