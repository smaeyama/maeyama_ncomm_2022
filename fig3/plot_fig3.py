#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import xarray

ds = xarray.open_dataset("data_netcdf/rr.nc")
rr = np.array(ds.rr)

ds = xarray.open_dataset("data_netcdf/zz.nc")
zz = np.array(ds.zz)

ds = xarray.open_dataset("data_netcdf/pres.nc")
pres = np.array(ds.pres)

ds = xarray.open_dataset("data_netcdf/phi.nc")
phi = np.array(ds.phi)

ds = xarray.open_dataset("data_netcdf/exb_velocity_closeup.nc")
r3 = np.array(ds.r_closeup)
z3 = np.array(ds.z_closeup)
vr3 = np.array(ds.vr)
vz3 = np.array(ds.vz)


# In[ ]:


eps_r=0.18
# zz=0.0
fcs=1.0 # For electron
Znum=1.0 # For electron
tau=3.0 # For electron, T_e/T_i

ds = xarray.open_dataset("data_netcdf/fluxinvm.nc")
vl = np.array(ds.vl)
vp = np.array(ds.vp)
fluxinvm = np.array(ds.fluxinvm)
vl2, vp2 = np.meshgrid(vl,vp)

def func_omg(zz):
    omg=1.0 - eps_r * np.cos(zz)
    return omg
omg=func_omg(zz=0.0)
omg_max=func_omg(np.pi)

def vp_trapped_boundary(vl,omg,omg_max):
    vp_bound=np.sqrt(vl**2/(omg_max/omg - 1))
    return vp_bound

def vp_magnetic_drift_resonance(vl,zz,kx,ky,tau,Znum,s_hat,real_freq):
    """
    When kx=0 and real_freq/ky=const, ky-dependence dissapears.
    """
    vp_magnetic_reso=np.sqrt(2*(real_freq*Znum/(tau*(ky*(np.cos(zz)+s_hat*zz*np.sin(zz))+kx*np.sin(zz))) - vl**2))
    return vp_magnetic_reso


# In[ ]:


plt.style.use('../nature_style.txt')

fig=plt.figure(figsize=(7.2,6.2),dpi=600)
gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=(2,1), hspace=0.3)

### Fig.2a ###
ax1=fig.add_subplot(gs[0,0])
xl=0.75;xr=1.25;
ax1.set_xlim(xl,xr)
yb=-0.25;yu=0.25
ax1.set_ylim(yb,yu)
ax1.set_aspect("equal")
quad1=ax1.pcolormesh(rr,zz,pres[:,:],cmap="hot",shading="auto")
quadc=ax1.contour(rr,zz,phi[:,:],colors="k",linestyles="solid",linewidths=0.3,alpha=1,levels=5)
vmax=np.max(np.abs(pres[:,:])) * 1.0
quad1.set_clim(-vmax,vmax)
ax1.set_xlabel(r"Major radius $R$ ($R_0$)")
ax1.set_ylabel(r"Height $Z$ ($R_0$)")
cax=ax1.inset_axes([1.25,0,0.75,0.05])
cbar=fig.colorbar(quad1,orientation="horizontal",cax=cax)
cbar.set_label(r"Perturbed electron pressure $\tilde{p}_e$ ($\rho_\mathrm{ti}n_\mathrm{e}T_\mathrm{i}/R_0$)")#+" (t={})".format(time))

### Fig.2b ###
xs=1.25
ys=0.25
ws=0.75
axins = ax1.inset_axes([xs, ys, ws, ws*(xr-xl)/(yu-yb)])
quads=axins.pcolormesh(rr,zz,pres[:,:],cmap="hot",shading="auto")
quads.set_clim(-vmax,vmax)
quadcs=axins.contour(rr,zz,phi[:,:],colors="k",linestyles="solid",linewidths=0.5,alpha=0.5,levels=30)
#axins.streamplot(r3,z3,vr3,vz3,density=[3,3],color="k",linewidth=0.3,arrowsize=0.6,arrowstyle="-|>, head_length=0.5",minlength=0.2)

### Draw ExB flow vector ###
### - Normalization
vel_max=np.sqrt(vr3**2+vz3**2).std()
wvr=vr3/vel_max
wvz=vz3/vel_max
wvel=np.sqrt(wvr**2+wvz**2)
### - Reduce grids (by qskip). Deminish data to zero when ExB flow is small (by wfilter)
wfilter=np.where(np.abs(wvel)<1.5, 0, 1)
qskip=20
wr3,wz3=np.meshgrid(r3[::qskip],z3[::qskip])
wvr=(wfilter*wvr)[::qskip,::qskip]
wvz=(wfilter*wvz)[::qskip,::qskip]
wvel=(wfilter*wvel)[::qskip,::qskip]
### - Do not plot when velocity is zero.
mask = np.logical_or(wvr!=0,wvz!=0)
wr3=wr3[mask]
wz3=wz3[mask]
wvr=wvr[mask]
wvz=wvz[mask]
wvel=wvel[mask]
quiv=axins.quiver(wr3,wz3,wvr,wvz,wvel,cmap="winter_r",width=0.01,alpha=1)

xl_s=1.12
yb_s=-0.02
lw_s=0.04
axins.set_xlim(xl_s,xl_s+lw_s)
axins.set_ylim(yb_s,yb_s+lw_s)

# xticks = axins.get_xticks()
# yticks = axins.get_yticks()
xticks = np.linspace(xl_s,xl_s+lw_s,5)
yticks = np.linspace(yb_s,yb_s+lw_s,5)
rho=0.1056338E-002
axins.set_xticks(xticks)
axins.set_xticklabels(np.round((xticks-(xticks[-1]+xticks[0])/2)/rho,1))
axins.set_yticks(yticks)
axins.set_yticklabels(np.round(yticks/rho,1))
axins.set_xlabel(r"Radial direction $x$ ($\rho_\mathrm{ti}$)")
axins.set_ylabel(r"Poloidal direction $y$ ($\rho_\mathrm{ti}$)")

ax1.indicate_inset_zoom(axins,linewidth=1,alpha=1,edgecolor="lime")


### Fig.2c ###
# ax=fig.add_subplot(gs[1,0])
# pos=ax.get_position()
# print(pos)
ax2=fig.add_axes([0.06, 0.11, 0.775, 0.22])
ax2.set_xlim(-4,4)
ax2.set_ylim(0,4)
ax2.set_xticks(np.linspace(-4,4,9))
ax2.set_aspect("equal")
vmax=np.max(np.abs(0.5*(vl2**2+vp2**2)*fluxinvm[:,:]*fcs/Znum*tau))
quad2=ax2.pcolormesh(vl,vp,0.5*(vl2**2+vp2**2)*fluxinvm[:,:]*fcs/Znum*tau,cmap="RdBu_r",shading="auto")
quad2.set_clim(-vmax,vmax)
cbar=fig.colorbar(quad2,shrink=1,aspect=10,pad=0.02)
ax2.set_title(r"Velocity-space dependent energy flux $Q^v_\mathrm{e}$ ($Q_\mathrm{gB}/v_\mathrm{te}^3$)",fontsize=7)#" (at $\theta=${:.0f}, ".format(zz/np.pi)+r"$100<tv_\mathrm{ref}/R_0<200$)")
ax2.set_xlabel(r"Parallel velocity $v_\parallel$ ($v_\mathrm{te}$)")
ax2.set_ylabel(r"Perpendicular velocity $v_\perp$ ($v_\mathrm{te}$)")
wvl=np.linspace(-5,5,513)
ax2.plot(wvl,vp_trapped_boundary(wvl,omg,omg_max),c="g",lw=1)
#ax2.plot(wvl,vp_magnetic_drift_resonance(wvl,zz=0.0,kx=0,ky=4.5,tau=3,Znum=1,s_hat=0.8,real_freq=24.29121),ls="dashed",c="k",lw=1) # ETG
ax2.plot(wvl,vp_magnetic_drift_resonance(wvl,zz=0.0,kx=0,ky=0.2,tau=3,Znum=1,s_hat=0.8,real_freq=1.141965),ls="dashed",c="k",lw=1) # TEM


fig.text(0.32,0.89,"a",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.80,0.89,"b",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)
fig.text(0.32,0.355,"c",color="k", fontfamily="sans-serif", fontweight="bold", fontsize=8)


plt.savefig("fig3.jpg",dpi=600)
quad1.set_rasterized(True)
quads.set_rasterized(True)
quad2.set_rasterized(True)
plt.savefig('fig3.svg',bbox_inches="tight")
import subprocess
subprocess.call('inkscape fig3.svg -M fig3.emf', shell=True)
subprocess.call('inkscape fig3.svg -E fig3.eps', shell=True)
subprocess.call('inkscape fig3.svg -A fig3.pdf', shell=True)
plt.show()


# In[ ]:




