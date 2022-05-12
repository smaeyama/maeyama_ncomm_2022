#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

ds=xr.open_dataset("data_netcdf/subspace_trans.nc")
# print(ds)
# tau = 3.0

plt.style.use('../nature_style.txt')

fig=plt.figure(figsize=(3.3,4.5),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)
ax1=fig.add_subplot(211)
var=ds.jkee
# vmax=np.abs(var).max()
vmax=np.abs(ds.jkie+ds.jkei).max()*0.2
quad1=ax1.pcolormesh(ds.kx,ds.ky,var,cmap="seismic",shading="auto",vmin=-vmax,vmax=vmax)
fig.colorbar(quad1,shrink=0.83,aspect=10)
ax1.set_xlim(-4,4)
ax1.set_ylim(0,5)
ax1.set_xlabel(r"Radial wave number $k_x \rho_\mathrm{ti}$")
ax1.set_ylabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
ax1.set_aspect("equal")
ax1.set_title(r"Electron-scale, electron-scale coupling $J_{\bf k}^{\Omega_e,\Omega_e}$",fontsize=7)

ax2=fig.add_subplot(212)
var=ds.jkie+ds.jkei
# vmax=np.abs(var).max()
quad2=ax2.pcolormesh(ds.kx,ds.ky,var,cmap="seismic",shading="auto",vmin=-vmax,vmax=vmax)
fig.colorbar(quad2,shrink=0.83,aspect=10)
ax2.set_xlim(-4,4)
ax2.set_ylim(0,5)
ax2.set_xlabel(r"Radial wave number $k_x \rho_\mathrm{ti}$")
ax2.set_ylabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
ax2.set_aspect("equal")
ax2.set_title(r"Ion-scale, electron-scale coupling $2J_{\bf k}^{\Omega_i,\Omega_e}$",fontsize=7)

fig.text(0.06,0.87,"a",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.06,0.455,"b",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)

plt.savefig("fig5.jpg",dpi=600)
quad1.set_rasterized(True)
quad2.set_rasterized(True)
plt.savefig('fig5.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig5.svg -M fig5.emf', shell=True)
subprocess.call('inkscape fig5.svg -E fig5.eps', shell=True)
subprocess.call('inkscape fig5.svg -A fig5.pdf', shell=True)
plt.show()


# In[ ]:




