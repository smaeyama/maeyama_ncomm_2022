#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("data/lin_eDTHe_Te010_LB_kyscan.dat")
data2 = np.loadtxt("data/lin_eDTHe_Te020_LB_kyscan.dat")
data3 = np.loadtxt("data/lin_eDTHe_Te030_LB_kyscan.dat")
data4 = np.loadtxt("data/lin_eDTHe_Te040_LB_kyscan.dat")

### Extract only positive linear growthrate
# data1 = data1[(data1[:,3]>0),:]
# data2 = data2[(data2[:,3]>0),:]
# data3 = data3[(data3[:,3]>0),:]
# data4 = data4[(data4[:,3]>0),:]

plt.style.use('../nature_style.txt')

fig=plt.figure(figsize=(6.6,5.0),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)

tau = 1.0
ax=fig.add_subplot(221)
# ax.set_xlabel(r"Poloidal wavenumber $k_y$ ($\rho_\mathrm{ti}^{-1}$)")
ax.set_ylabel(r"Linear growth rate $\gamma$ ($v_\mathrm{ti}/R_0$), "+"\n"+r"real frequency $\omega_\mathrm{r}$ ($v_\mathrm{ti}/R_0$)")
ax.plot(data1[20:,1],data1[20:,3],"o-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=1, \gamma$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data1[20:,1],data1[20:,2]/40,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=1, \omega_\mathrm{r}/40$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(1e-2,20)
ax.legend()

tau = 2.0
ax=fig.add_subplot(222)
# ax.set_xlabel(r"Poloidal wavenumber $k_y$ ($\rho_\mathrm{ti}^{-1}$)")
# ax.set_ylabel(r"Linear growth rate $\gamma$ ($v_\mathrm{ti}/R_0$), "+"\n"+r"real frequency $\omega_\mathrm{r}$ ($v_\mathrm{ti}/R_0$)")
ax.plot(data2[8:,1],data2[8:,3],"o-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=2, \gamma$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data2[8:,1],data2[8:,2]/40,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=2, \omega_\mathrm{r}/40$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(1e-2,20)
ax.legend()

tau = 3.0
ax=fig.add_subplot(223)
ax.set_xlabel(r"Poloidal wavenumber $k_y$ ($\rho_\mathrm{ti}^{-1}$)")
ax.set_ylabel(r"Linear growth rate $\gamma$ ($v_\mathrm{ti}/R_0$), "+"\n"+r"real frequency $\omega_\mathrm{r}$ ($v_\mathrm{ti}/R_0$)")
ax.plot(data3[1:9,1],data3[1:9,3],"o-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=3, \gamma$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data3[10:,1],data3[10:,3],"o-",c="C0",label="",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data3[1:9,1],data3[1:9,2]/40,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=3, \omega_\mathrm{r}/40$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data3[10:,1],data3[10:,2]/40,"^-",c="C1",label="",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(1e-2,20)
ax.legend()

tau = 4.0
ax=fig.add_subplot(224)
ax.set_xlabel(r"Poloidal wavenumber $k_y$ ($\rho_\mathrm{ti}^{-1}$)")
# ax.set_ylabel(r"Linear growth rate $\gamma$ ($v_\mathrm{ti}/R_0$), "+"\n"+r"real frequency $\omega_\mathrm{r}$ ($v_\mathrm{ti}/R_0$)")
ax.plot(data4[:9,1],data4[:9,3],"o-",c="C0",label=r"$T_\mathrm{e}/T_\mathrm{i}=4, \gamma$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data4[:9,1],data4[:9,2]/40,"^-",c="C1",label=r"$T_\mathrm{e}/T_\mathrm{i}=4, \omega_\mathrm{r}/40$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05,40)
ax.set_ylim(1e-2,20)
ax.legend()

fig.text(0.125,0.89,"a",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.55,0.89,"b",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.125,0.48,"c",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.55,0.48,"d",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)

plt.savefig("supple_fig1.jpg",dpi=600)
plt.savefig('supple_fig1.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape supple_fig1.svg -M supple_fig1.emf', shell=True)
subprocess.call('inkscape supple_fig1.svg -E supple_fig1.eps', shell=True)
subprocess.call('inkscape supple_fig1.svg -A supple_fig1.pdf', shell=True)
plt.show()


# In[ ]:




