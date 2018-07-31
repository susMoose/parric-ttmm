#! /usr/bin/bash
if [ $# -ne 2 ]
then
	echo "usage: $0 <size> <iterations>"
	exit 1
fi
min=100000000
N=$1
let "b1 = $N / 2"
let "b2 = $N / 2"
let "b3 = $N / 2"
let "step = $N / 4"

cd ttmm/alphaz_stuff/out
for ((iterations=1;iterations<=$2;iterations++))
do
	for ts1 in {0..1}
	do
		let "local_1 = ($b1 + ( (2 * $ts1) - 1 ) * $step )"
		for ts2 in {0..1}
		do
			let "local_2 = ($b2 + ( (2 * $ts2) - 1 ) * $step )"
			for ts3 in {0..1}
			do
				let "local_3 = ($b3 + ( (2 * $ts3) - 1 ) * $step )"
				time=$(./TMM $N $local_1 $local_2 $local_3 | grep -E -e "[0-9]+(.[0-9]+)?" -o)	
				echo "./TMM $N $local_1 $local_2 $local_3 | grep -E -e [0-9]+(.[0-9]+)? -o"
				if [ $(echo "$min > $time"|bc) -eq 1 ]
				then
					min=$time
					next_b1=$local_1
					next_b2=$local_2
					next_b3=$local_3
				fi
			done
		done
	done
	
	let "step = $step / 2"
	b1=$next_b1
	b2=$next_b2
	b3=$next_b3
	
	echo "best: $min ($b1, $b2, $b3)"
done
