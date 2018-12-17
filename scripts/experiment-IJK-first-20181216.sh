echo 'python3 commander.py  -f experiment-config --path-prefix ./workspace/parric-ttmm/parallelTests/ijk/out/firstLoop | tee -a ~/workspace/parric-ttmm/results/experiment-IJK-first-20181216.log' 
echo ''
python3 commander.py \
-f experiment-config \
--path-prefix ./workspace/parric-ttmm/parallelTests/ijk/out/firstLoop \
| tee -a ~/workspace/parric-ttmm/results/experiment-IJK-first-20181216.log
