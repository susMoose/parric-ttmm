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

cd ttmm/alphaz_stuff/out
for ts1 in {0..1}
do
	let "local_1 = ($lower_bound1 + ($mid1/2) + ($ts1 * $mid1))"
	for ts2 in { 0..1}
	do
		let "local_2 = ($lower_bound2 + ($mid2/2) + ($ts2 * $mid2))"
		for ts3 in {0..1}
		do
			let "local_3 = ($lower_bound3 + ($mid3/2) + ($ts3 * $mid3))"
			time=$(./TTMM $N $local_1 $local_2 $local_3 | grep -E -e "\d+(.\d+)?" -o)
			if [ $min -gt $time ]
			then
				min=$time
				let "upper_bound1 = $local_1 + ( $mid1 /  2)"	
				let "lower_bound1 = $local_1 - ( $mid1 /  2)"
