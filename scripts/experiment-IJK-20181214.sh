echo 'unbuffer python3 commander.py -N 5000 --parent-center 500 500 500 --parent-size 1000 -i 4 --partitions 4 4 4 4 -k 16 4 2 2 --path-prefix ./workspace/parric-ttmm/ttmm/ikj/out | tee -a ~/workspace/parric-ttmm/results/experiment-20180804.log'
echo ''
python3 commander.py \
-f experiment-TEST \
--path-prefix ./workspace/parric-ttmm/ttmm/ijk/out \
| tee -a ~/workspace/parric-ttmm/results/experiment-IJK-20181214.log
