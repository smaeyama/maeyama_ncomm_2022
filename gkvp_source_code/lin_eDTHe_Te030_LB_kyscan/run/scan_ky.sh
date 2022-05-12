#!/bin/sh

CURRENTDIR=`pwd`

param="1.00"

OLD_RUNDIR=`echo ${param} | awk '{printf("%s%05.2f","ky",$1)}'`
OLD_WKDIR="\/vol0006\/hp150279\/data\/u00165\/gkvp\/f0.59\/bpp\/lin\/lin_eDTHe_Te030_LB_kyscan\/${OLD_RUNDIR}"
kymin=`echo ${param} | awk '{printf("%5.2fd0",$1)}'`
OLD_PARAM="kymin = ${kymin},"

grep "$OLD_WKDIR" shoot &&\
grep "$OLD_PARAM" gkvp_namelist &&\
#for param in `seq 0.05 0.05 1.0`; do # ky scan  (ky = param)
for param in `seq 1.5 0.5 7.0`; do # ky scan  (ky = param)

 
  ### change working dir ###                                                                           ### for debug ###
  NEW_RUNDIR=`echo ${param} | awk '{printf("%s%05.2f","ky",$1)}'`;                                     echo ${NEW_RUNDIR}
  NEW_WKDIR="\/vol0006\/hp150279\/data\/u00165\/gkvp\/f0.59\/bpp\/lin\/lin_eDTHe_Te030_LB_kyscan\/${NEW_RUNDIR}"
  sed -i -e "s/${OLD_WKDIR}/${NEW_WKDIR}/g" shoot
 
  ### change parameter ###
  kymin=`echo ${param} | awk '{printf("%5.2fd0",$1)}'`
  NEW_PARAM="kymin = ${kymin},";                                                                       echo ${NEW_PARAM}
  sed -i -e "s/${OLD_PARAM}/${NEW_PARAM}/g" gkvp_namelist
 
  ### execution ###                                                                                    #################
  ./shoot 1 1

  OLD_WKDIR=${NEW_WKDIR}
  OLD_PARAM=${NEW_PARAM}
  

done
