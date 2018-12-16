#!/bin/bash

export OMP_NUM_THREADS=$1

make 

./TMM.verify-rand 5000 316 7 859
