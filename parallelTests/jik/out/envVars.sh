#!/bin/bash

export OMP_NUM_THREADS=$1

make 

./TMM 5000 316 7 849

