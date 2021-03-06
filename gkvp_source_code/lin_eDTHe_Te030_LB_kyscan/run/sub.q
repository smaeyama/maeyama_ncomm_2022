#!/bin/sh

###  NOTE  ###
###  Fugaku supercomputer, Environment III (Riken R-CCS, 2020)
###
###  - Computation nodes
###      CPU: A64FX (2.0GHz, 12coresx4CMG=48cores, 512bit SIMD) x1 per node
###      Peak performance: DP 3.072 TFLOPS per node (Boost: 3.3792 TFLOPS)
###      Cache L1: 64 KiB, 4 way
###      Cache L1 Bandwidth: 230+ GB/s(load), 115+ GB/s (store)
###      Cache L2: 8 MiB, 16 way per CMG(NUMA), 4CMG per node
###      Cache L2 Bandwidth: 3.6+ TB/s per node
###                          115+ GB/s(load), 57+ GB/s(store) per core
###      Memory: HBM2 32 GiB
###      Memory Bandwidth: 1024 GB/s per node
###
###      Therefore, a recommended GKV parallelization may be 
###          (MPI Processes)x(12 OpenMP Threads)
###          =(12 cores per CMG)x(4 CMG)x(Node numbers)
###      1 MPI process should be assigined to 1 CMG.
###
###  - Interconnect
###      Tofu Interconnect D (28 Gbps x 2 lane x 10 port)
###      [Performance] 8B Put latency: 0.49-0.54 usec
###                    1MiB Put throughput: 6.35 GB/s
###
###  - Job class (May 2020)
###      eap-large : 385 - 27648 nodes, 10 hour, Inf run/Inf submit
###      eap-small :   1 - 384   nodes, 10 hour, Inf run/Inf submit
###      eap-int   :   1 - 12    nodes,  6 hour, Inf run/3   submit, interactive
###
###  - Commands
###      (Submit a batch job : "pjsub sub.q") Use shoot script for GKV.
###      Check job status    : "pjstat" or "pjstat -E" for step jobs
###      Delete job          : "pjdel JOBID"
###      Show budget info    : "accountj"
###      Show disk usage     : "accountd"
##############

#### --rsc-list "rscunit=rscunit_ft01"
#PJM --rsc-list "rscgrp=small" # Job class     
#PJM --rsc-list "node=8"           # Number of nodes
#PJM --rsc-list "elapse=01:00:00"  # Execute time
#PJM --mpi "proc=32"               # Number of MPI (= Number of nodes x 4)
#### --mpi "rank-map-bynode"
#### --mpi "rank-map-hostfile=rankmapfile.dat"
#PJM -j                           # Write error in standard output file
#PJM -s                           # Job statistics

NUM_NODES=${PJM_NODE}             # Nodes
NUM_CORES=12                      # Cores per node
NUM_PROCS=$(( ${NUM_NODES} * 4 )) # MPI processes
export OMP_NUM_THREADS=12         # OpenMP threads per MPI


echo "                  Nodes: ${NUM_NODES}"
echo "         Cores per node: ${NUM_CORES}"
echo "          MPI Processes: ${NUM_PROCS}"
echo " OpenMP threads per MPI: ${OMP_NUM_THREADS}"



### Working directory 
DIR=%%DIR%%
LDM=gkvp_mpifft.exe
NL=gkvp_namelist.%%%

#export XOS_MMM_L_PAGING_POLICY=demand:demand:demand # For Largepage

export PLE_MPI_STD_EMPTYFILE="off" # Suppress stdout of filesize-0

#### Run
date
cd ${DIR}
export fu05=${DIR}/${NL}
mpiexec -n ${NUM_PROCS} ${DIR}/${LDM}
#mpiexec -std ${JOBNAME}.${JOBID}.out -n ${NUM_PROCS} ${DIR}/${LDM}
#mpiexec --std %n.%j -n ${NUM_PROCS} ${DIR}/${LDM}
   # -n        "Total number of MPI processes"
date


##### Run with Fujitsu profiler fipp (re-compile with -Nfjprof option)
#date
#cd ${DIR}
#export fu05=${DIR}/${NL}
#fipp -C -d ${DIR}/fjprof_dir/pa0 -Icpupa -Impi -Sregion  mpiexec -n ${NUM_PROCS} ${DIR}/${LDM}
#date
#echo "#!/bin/sh" > ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "set -Ceu" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "set -x" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "fipppx -A -d pa0 -Icpupa     -p0,limit=4 -o prof_cpupa.txt" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "fipppx -A -d pa0 -Ibalance   -p0,limit=4 -o prof_balance.txt" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "#fipppx -A -d pa0 -Icall      -p0,limit=4 -o prof_call.txt" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh
#echo "fipppx -A -d pa0 -Isrc:./src -p0,limit=4 -o prof_src.txt" >> ${DIR}/fjprof_dir/fugaku_fipppx.sh


##### Run with Fujitsu profiler fapp (re-compile with -Nfjprof option)
#date
#cd ${DIR}
#export fu05=${DIR}/${NL}
#Npa=1  # Elementary report
##Npa=5  # Simple report
##Npa=11 # Standard report
##Npa=17 # Detailed report
#for i in `seq 1 ${Npa}`; do
#  echo "pa"${i} `date`
#  fapp -C -d ${DIR}/fjprof_dir/pa${i} -Hevent=pa${i} -Sregion  mpiexec -n ${NUM_PROCS} ${DIR}/${LDM}
#done
#date
#
#echo "#!/bin/sh" > ${DIR}/fjprof_dir/fugaku_fapppx.sh
#for i in `seq 1 ${Npa}`; do
#  echo "fapppx -A -d ./pa${i} -Icpupa,mpi -tcsv -o pa${i}.csv" >> ${DIR}/fjprof_dir/fugaku_fapppx.sh
#done
#echo "cp /opt/FJSVxtclanga/tcsds-1.2.25/misc/cpupa/cpu_pa_report.xlsm ./" >> ${DIR}/fjprof_dir/fugaku_fapppx.sh
#
#
