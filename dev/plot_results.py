
import xarray as xr 
import numpy as np
from matplotlib import pyplot as plt
import cartopy.crs as ccrs

def plot_trajectories(output_file: str) -> None:
    # Open the output file as a pandas dataframe using xarray
    output = xr.open_zarr(output_file) #.to_dataframe() 

    x = output["lon"].values
    y = output["lat"].values

    real_time = output["time"].values.astype("datetime64[h]")
    time_since_release = real_time - real_time[0,0]

    print(time_since_release.shape, x.shape, y.shape)
    
    #plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    #ax.set_extent([13,15.2,67.6,68.7])
    for  i in range(len(x)):
        ax.plot(x[i,:], y[i,:], transform=ccrs.Geodetic(), lw=.2)
    
    plt.tight_layout()
    plt.savefig("testsim.png")

filename = "testsim.zarr"
plot_trajectories(filename)