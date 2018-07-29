#! /usr/bin/bash

min=100000000
N=5000
upper_bound1=$N
lower_bound1=0
let "mid1 = $upper_bound1 - $lower_bound1"
let "mid1 = $mid1 / 2"

upper_bound2=$N
lower_bound2=0
let "mid2 = $upper_bound2 - $lower_bound2"
let "mid2 = $mid2 / 2"

upper_bound3=$N
lower_bound3=0
let "mid3 = $upper_bound3 - $lower_bound3"
let "mid3 = $mid3 / 2"

b1=-5
b2=-5
b3=-5

cd ttmm/alphaz_stuff/out
for iterations in {1..6}
do
	old_min=$min
	for ts1 in {0..1}
	do
		let "local_1 = ($lower_bound1 + ($mid1/2) + ($ts1 * $mid1))"
		for ts2 in {0..1}
		do
			let "local_2 = ($lower_bound2 + ($mid2/2) + ($ts2 * $mid2))"
			for ts3 in {0..1}
			do
				let "local_3 = ($lower_bound3 + ($mid3/2) + ($ts3 * $mid3))"
				time=$(./TMM $N $local_1 $local_2 $local_3 | grep -E -e "[0-9]+(.[0-9]+)?" -o)	
				echo "./TMM $N $local_1 $local_2 $local_3 | grep -E -e [0-9]+(.[0-9]+)? -o"
				if [ $(echo "$min > $time"|bc) -eq 1 ]
				then
					min=$time
					b1=$local_1
					b2=$local_2
					b3=$local_3
				fi
			done
		done
	done
	if [ $old_min = $min ]
	then
		echo "no new min; exiting"
		exit 0
	fi
	
	let "upper_bound1 = $b1 + ( $mid1 /  2)"	
	let "lower_bound1 = $b1 - ( $mid1 /  2)"
	let "upper_bound2 = $b2 + ( $mid2 /  2)"	
	let "lower_bound2 = $b2 - ( $mid2 /  2)"

	let "upper_bound3 = $b3 + ( $mid3 /  2)"	
	let "lower_bound3 = $b3 - ( $mid3 /  2)"

	let "mid1 = $mid1 / 2"
	let "mid2 = $mid2 / 2"
	let "mid3 = $mid3 / 2"

	echo "best: $min ($b1, $b2, $b3)"
done
