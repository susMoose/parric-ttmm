MKL_FLAGS=-I/s/parsons/l/sys/intel/mkl/include/ -L/s/parsons/l/sys/intel/compilers_and_libraries_2018.0.128/linux/mkl/lib/intel64  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core  -L/s/parsons/l/sys/intel/lib/intel64 -liomp5 -lm

#SIZE=10

TMM:TMM-wrapper.c TMM.o blockformat.o
	gcc $^ -o $@ -O3 $(MKL_FLAGS)

check: TMM-wrapper.c TMM.o blockformat.o
	gcc $^ -o TMM.check -O3 $(MKL_FLAGS) -DCHECKING

correctness: clean
	g++ blockformat.c -c  -DSIZE=$(SIZE) -O3 -o blockformat.o -Wfatal-errors
	g++ TMM.c -o TMM.o -O3 $(MKL_FLAGS) -DSIZE=$(SIZE) -c
	g++ testStuff.cpp -o TMM.check TMM.o blockformat.o $(MKL_FLAGS) -DCHECKING
TMM.o:TMM.c
	gcc $^ -o $@ -O3 $(MKL_FLAGS) -DSIZE=$(SIZE) -c

runTMM: TMM
	$$(./mkl_setup.sh) ; \
	./TMM 5000 5000 5000 5000

runcheck: check
	$$(./mkl_setup.sh) ; \
	./TMM.check 4 4 4 4

testBlockFormat:testBlockFormat.c blockformat.o
	gcc $^  -o $@ -DTEST_SIZE=31

blockformat.o: blockformat.c
	gcc $< -c  -DSIZE=$(SIZE) -O3 -o $@ -Wfatal-errors

clean:
	rm -f ./*.o TMM
