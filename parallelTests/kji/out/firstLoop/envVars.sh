#!/bin/bash

export OMP_NUM_THREADS=$1

make 

#./TMM 5000 316 7 849 
./TMM.verify-rand 100  20 20 20 
./TMM.verify-rand 5000 316 7 849

export OMP_NUM_THREADS=1
#./TMM.verify-rand 100  20 20 20 
./TMM.verify-rand 5000 316 7 849
