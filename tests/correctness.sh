cd ../ttmm/alphaz_stuff
./cmdlinecompile.sh
cd out
cp Makefile.old Makefile
make check
./TMM.check 1000 2>correctness_err.txt
words=$(wc -w correctness_err.txt |grep -E -e "[0-9]+" -o)
if [ $words -gt 0 ]
then 
	exit 1
fi
echo "No Errors."
