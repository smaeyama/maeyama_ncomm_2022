#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("lin_eDTHe_Te030_LB_kyscan.dat")

plt.style.use('../nature_style.txt')
fig=plt.figure(figsize=(3.3,2.5),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)
plt.style.use('../nature_style.txt')


ax=fig.add_subplot(111)
ax.set_xlabel(r"Poloidal wavenumber $k_y$ ($\rho_\mathrm{ti}^{-1}$)")
ax.set_ylabel(r"Linear growth rate $\gamma$ ($v_\mathrm{ti}/R_0$), "+"\n"+r"real frequency $\omega_\mathrm{r}$ ($v_\mathrm{ti}/R_0$)")
ax.plot(data[:,1],data[:,3],"o-",label=r"$\gamma$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.plot(data[:,1],data[:,2]/40,"o-",label=r"$\omega_\mathrm{r}/40$",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend()

plt.savefig("fig1.jpg",dpi=600)
plt.savefig('fig1.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig1.svg -M fig1.emf', shell=True)
subprocess.call('inkscape fig1.svg -E fig1.eps', shell=True)
subprocess.call('inkscape fig1.svg -A fig1.pdf', shell=True)
plt.show()


# In[ ]:




