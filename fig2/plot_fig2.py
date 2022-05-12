#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

eps_r    = 0.18
q_0      = 1.42

ds1 = xr.open_dataset("data_netcdf/txE_resonant_multiscale.nc")
ds2 = xr.open_dataset("data_netcdf/txE_resonant_woelectronscale.nc")
ds3 = xr.open_dataset("data_netcdf/txE_offresonant_multiscale.nc")
ds4 = xr.open_dataset("data_netcdf/txE_offresonant_woelectronscale.nc")
ds_list = [ds1, ds2, ds3, ds4]


# In[ ]:


fig=plt.figure(figsize=(3.4,2.5),dpi=600) # figsize=(幅,高さ(inch)),dpi(dots per inch)
plt.style.use('../nature_style.txt')

###
label = [r"Resonant $v=2v_\mathrm{te}$ (Multi-scale)", 
         r"Resonant $v=2v_\mathrm{te}$ (w/o electron-scale)", 
         r"Off-resonant $v=2.5v_\mathrm{te}$ (Multi-scale)", 
         r"Off-resonant $v=2.5v_\mathrm{te}$ (w/o electron-scale)"]
color = ["tab:red", "k", "b", "tab:green"]
linestyle = ["solid", "dashed", "solid", "dashed"]
ax=fig.add_subplot(211)
ax.axes.xaxis.set_ticklabels([])
ax.set_ylabel("Poloidal electric \n field "+r"$E_y$ ($T_\mathrm{i}/eR_0$)")
for i in range(4):
    ds = ds_list[i]
    y = ds.y
    j0Ey = ds.j0Ey
    ax.plot((y-y[0])*q_0/eps_r,j0Ey,label=label[i],c=color[i],linestyle=linestyle[i],lw=1)
ax.axhline(0,c="k",lw=0.5)
ax.set_xlim(0,1450)
ax.set_ylim(-20,20)
ax.set_yticks([-15,0,15])
fig.legend(loc="lower left",ncol=1,bbox_to_anchor=(0.15,0.88),labelspacing=0)
ax=fig.add_subplot(212)
ax.set_xlabel(r"Toroidal path length $y q / \epsilon_r$ ($\rho_\mathrm{ti}$)")
ax.set_ylabel("Radial\n displacement\n" + r"$x$ ($\rho_\mathrm{ti}$)")
for i in range(4):
    ds = ds_list[i]
    y = ds.y
    x = ds.x
    ax.plot((y-y[0])*q_0/eps_r,x-x[0],label=label[i],c=color[i],linestyle=linestyle[i],lw=1)
ax.axhline(0,c="k",lw=0.5)
ax.set_xlim(0,1450)
ax.set_ylim(-15,50)
ax.set_yticks([0,20,40])

fig.text(0.045,0.885,"a",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.045,0.460,"b",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)

plt.savefig("fig2.jpg",dpi=600)
plt.savefig('fig2.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig2.svg -M fig2.emf', shell=True)
subprocess.call('inkscape fig2.svg -E fig2.eps', shell=True)
subprocess.call('inkscape fig2.svg -A fig2.pdf', shell=True)
plt.show()


# In[ ]:





# In[ ]:




