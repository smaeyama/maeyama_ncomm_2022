#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

ds3m=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_x0512y0512z20v32m15_qes.0.nc")
ds3i=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_x0128y0032z20v32m15_qes.0.nc")
ds3e=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_ele_x0256y0064z20v32m15_qes.0.nc")
### Note that data of the electron heat flux $Q_e$ is normalized by $n_0T_iv_{ti}\rho_{ti}^2/R^2$".
tau = 3.0

plt.style.use('../nature_style.txt')

fig=plt.figure(figsize=(3.3,2.5),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)
ax=fig.add_subplot(111)
ax.set_xlabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
ax.set_ylabel(r"Electron energy flux $Q_{\mathrm{e}k}/(\Delta k_y \rho_\mathrm{ti})$ ($Q_\mathrm{gB}$)")
ax.plot(ds3m.ky,ds3m.qes/ds3m.ky[1]/tau/np.sqrt(tau)**3,"s-",label="Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds3i.ky,ds3i.qes/ds3i.ky[1]/tau/np.sqrt(tau)**3,"^-",label="Ion-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds3e.ky[1:],ds3e.qes[1:]/ds3e.ky[1]/tau/np.sqrt(tau)**3,"o-",label="Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,20)
ax.set_ylim(0.5e-3,1e3)
ax.legend()

plt.savefig("fig4.jpg",dpi=600)
plt.savefig('fig4.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig4.svg -M fig4.emf', shell=True)
subprocess.call('inkscape fig4.svg -E fig4.eps', shell=True)
subprocess.call('inkscape fig4.svg -A fig4.pdf', shell=True)
plt.show()

print(r"$Q_gB = n_0 T_e c_a \rho_a^2/R^2$ defined.")


# In[ ]:




