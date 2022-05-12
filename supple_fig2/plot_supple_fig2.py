#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

ds1m=xr.open_dataset("data_netcdf/nl_eDTHe_Te010_x1024y1024z20v32m15_qes.0.nc")
ds1e=xr.open_dataset("data_netcdf/nl_eDTHe_Te010_ele_kymin100_x0256y0064z20v32m15_qes.0.nc")
ds2m=xr.open_dataset("data_netcdf/nl_eDTHe_Te020_x0512y0512z20v32m15_qes.0.nc")
ds2e=xr.open_dataset("data_netcdf/nl_eDTHe_Te020_ele_x0256y0064z20v32m15_qes.0.nc")
ds3m=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_x0512y0512z20v32m15_qes.0.nc")
ds3i=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_x0128y0032z20v32m15_qes.0.nc")
ds3e=xr.open_dataset("data_netcdf/nl_eDTHe_Te030_ele_x0256y0064z20v32m15_qes.0.nc")
ds4m=xr.open_dataset("data_netcdf/nl_eDTHe_Te040_x0512y0512z20v32m15_qes.0.nc")
ds4i=xr.open_dataset("data_netcdf/nl_eDTHe_Te040_x0128y0032z20v32m15_qes.0.nc")
### Note that data of the electron heat flux $Q_e$ is normalized by $n_0T_iv_{ti}\rho_{ti}^2/R^2$".

plt.style.use('../nature_style.txt')

fig=plt.figure(figsize=(6.6,5.0),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)

tau = 1.0
ax=fig.add_subplot(221)
# ax.set_title(r"$T_\mathrm{e}/T_\mathrm{i}=1$")
# ax.set_xlabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
ax.set_ylabel(r"Electron energy flux $Q_{\mathrm{e}k}/(\Delta k_y \rho_\mathrm{ti})$ ($Q_\mathrm{gB}$)")
ax.plot(ds1m.ky,ds1m.qes/ds1m.ky[1]/tau/np.sqrt(tau)**3,"s-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=1$, Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds1e.ky[1:],ds1e.qes[1:]/ds1e.ky[1]/tau/np.sqrt(tau)**3,"o-",c="C2",label=r"$T_\mathrm{e}/T_\mathrm{i}=1$, Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(0.5e-3,1e3)
ax.legend()

tau = 2.0
ax=fig.add_subplot(222)
# ax.set_title(r"$T_\mathrm{e}/T_\mathrm{i}=2$")
# ax.set_xlabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
# ax.set_ylabel(r"Electron energy flux $Q_{\mathrm{e}k}/(\Delta k_y \rho_\mathrm{ti})$ ($Q_\mathrm{gB}$)")
ax.plot(ds2m.ky,ds2m.qes/ds2m.ky[1]/tau/np.sqrt(tau)**3,"s-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=2$, Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds2e.ky[1:],ds2e.qes[1:]/ds2e.ky[1]/tau/np.sqrt(tau)**3,"o-",c="C2",label=r"$T_\mathrm{e}/T_\mathrm{i}=2$, Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(0.5e-3,1e3)
ax.legend()

tau = 3.0
ax=fig.add_subplot(223)
# ax.set_title(r"$T_\mathrm{e}/T_\mathrm{i}=3$")
ax.set_xlabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
ax.set_ylabel(r"Electron energy flux $Q_{\mathrm{e}k}/(\Delta k_y \rho_\mathrm{ti})$ ($Q_\mathrm{gB}$)")
ax.plot(ds3m.ky,ds3m.qes/ds3m.ky[1]/tau/np.sqrt(tau)**3,"s-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=3$, Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds3i.ky,ds3i.qes/ds3i.ky[1]/tau/np.sqrt(tau)**3,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=3$, Ion-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds3e.ky[1:],ds3e.qes[1:]/ds3e.ky[1]/tau/np.sqrt(tau)**3,"o-",c="C2",label=r"$T_\mathrm{e}/T_\mathrm{i}=3$, Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(0.5e-3,1e3)
ax.legend()

tau = 4.0
ax=fig.add_subplot(224)
# # ax.set_title(r"$T_\mathrm{e}/T_\mathrm{i}=4$")
ax.set_xlabel(r"Poloidal wave number $k_y \rho_\mathrm{ti}$")
# ax.set_ylabel(r"Electron energy flux $Q_{\mathrm{e}k}/(\Delta k_y \rho_\mathrm{ti})$ ($Q_\mathrm{gB}$)")
ax.plot(ds4m.ky,ds4m.qes/ds4m.ky[1]/tau/np.sqrt(tau)**3,"s-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=4$, Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(ds4i.ky,ds4i.qes/ds4i.ky[1]/tau/np.sqrt(tau)**3,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=4$, Ion-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(0.5e-3,1e3)
ax.legend()

fig.text(0.125,0.89,"a",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.55,0.89,"b",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.125,0.48,"c",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.55,0.48,"d",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)

plt.savefig("supple_fig2.jpg",dpi=600)
plt.savefig('supple_fig2.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape supple_fig2.svg -M supple_fig2.emf', shell=True)
subprocess.call('inkscape supple_fig2.svg -E supple_fig2.eps', shell=True)
subprocess.call('inkscape supple_fig2.svg -A supple_fig2.pdf', shell=True)
plt.show()

print(r"$Q_gB = n_0 T_e c_a \rho_a^2/R^2$ defined.")


# In[ ]:




