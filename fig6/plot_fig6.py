#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

data = np.loadtxt("nl_qes_taudep.dat")
### Note that data of the electron heat flux $Q_e$ is normalized by $n_0T_iv_{ti}\rho_{ti}^2/R^2$".
tau, qe_multiscale, qe_multiscale_lowk, qe_multiscale_highk, qe_ionscale, qe_electronscale, std_multiscale, std_ionscale, std_electronscale = data.T

plt.style.use('../nature_style.txt')

# fig=plt.figure(figsize=(3.3,2.5),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)
# ax=fig.add_subplot(111)
# ax.set_xlabel(r"Temperature ratio $T_\mathrm{e}/T_\mathrm{i}$")
# ax.set_ylabel(r"Electron energy flux $Q_\mathrm{e}$ ($Q_\mathrm{gB}$)")
# ax.errorbar(tau,qe_multiscale/tau/np.sqrt(tau)**3,yerr=std_multiscale/tau/np.sqrt(tau)**3,fmt="s-",capsize=3,label="Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
# ax.errorbar(tau,qe_ionscale/tau/np.sqrt(tau)**3,yerr=std_ionscale/tau/np.sqrt(tau)**3,fmt="^-",capsize=3,label="Ion-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
# ax.errorbar(tau,qe_electronscale/tau/np.sqrt(tau)**3,yerr=std_electronscale/tau/np.sqrt(tau)**3,fmt="o-",capsize=3,label="Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
# ax.set_ylim(0,None)
# ax.legend()
# plt.show()

# Normalized by $Q_gB = n_0 T_e c_a \rho_a^2/R^2$
qe_multiscale_normalized = qe_multiscale/tau/np.sqrt(tau)**3
qe_ionscale_normalized = qe_ionscale/tau/np.sqrt(tau)**3
qe_electronscale_normalized = qe_electronscale/tau/np.sqrt(tau)**3
std_multiscale_normalized = std_multiscale/tau/np.sqrt(tau)**3
std_ionscale_normalized = std_ionscale/tau/np.sqrt(tau)**3
std_electronscale_normalized = std_electronscale/tau/np.sqrt(tau)**3

qe_min=1e-1
# Undefined small values are replaced by qe_min.
qe_multiscale_normalized = np.where(qe_multiscale_normalized < qe_min, qe_min, qe_multiscale_normalized)
qe_ionscale_normalized = np.where(qe_ionscale_normalized < qe_min, qe_min, qe_ionscale_normalized)
qe_electronscale_normalized = np.where(qe_electronscale_normalized < qe_min, qe_min, qe_electronscale_normalized)
# Too lrage standard deviation for the case Te/Ti=1 electron-scale simulation is suppressed for visibility.
std_electronscale_normalized[0]=0
# NOTE: The above two modifications are explicitly stated in the figure caption.

fig=plt.figure(figsize=(3.3,2.5),dpi=600) # figsize=(width,height(inch)),dpi(dots per inch)
ax=fig.add_subplot(111)
ax.set_xlabel(r"Temperature ratio $T_\mathrm{e}/T_\mathrm{i}$")
ax.set_ylabel(r"Electron energy flux $Q_\mathrm{e}$ ($Q_\mathrm{gB}$)")
ax.errorbar(tau,qe_multiscale_normalized,yerr=std_multiscale_normalized,fmt="s-",capsize=3,label="Multi-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.errorbar(tau,qe_ionscale_normalized,yerr=std_ionscale_normalized,fmt="^-",capsize=3,label="Ion-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.errorbar(tau,qe_electronscale_normalized,yerr=std_electronscale_normalized,fmt="o-",capsize=3,label="Electron-scale sim.",markeredgecolor="k",markersize=4,markeredgewidth=0.3)
ax.set_ylim(qe_min,3e2)
ax.set_yscale("log")
ax.legend()

plt.savefig("fig6.jpg",dpi=600)
plt.savefig('fig6.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig6.svg -M fig6.emf', shell=True)
subprocess.call('inkscape fig6.svg -E fig6.eps', shell=True)
subprocess.call('inkscape fig6.svg -A fig6.pdf', shell=True)
plt.show()

print(r"$Q_gB = n_0 T_e c_a \rho_a^2/R^2$ defined.")


# In[ ]:




