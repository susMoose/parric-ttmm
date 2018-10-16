#include <stdio.h>
#include <stdlib.h>
#include "omp.h"
#include <sys/time.h>
#include <inttypes.h>

#define N 100000000
double dot(double * restrict A, double * restrict B) {
	double *AA = __builtin_assume_aligned(A,16);
	double *BB = __builtin_assume_aligned(B,16);
	double sum = 0.0;
	for (int i=0; i<N; i++) {
		sum += AA[i] * BB[i];
	}
	return sum;
}

double dot_parallel(double * restrict A, double * restrict B) {
    double *AA = __builtin_assume_aligned(A,16);
    double *BB = __builtin_assume_aligned(B,16);
	double sum = 0.0;
#pragma omp parallel for reduction(+:sum)
    for (int i=0; i<N; i++) {
        sum += AA[i] * BB[i];
    }
	return sum;
}   

void populate_array(double *T) {
	for (int i=0; i<N; i++) {
		T[i] = ((double)rand()/(double)(RAND_MAX)) * 5 - 2.5;
	}
}

int main() {
	double *A = (double*)malloc(sizeof(double)*N);
	double *B = (double*)malloc(sizeof(double)*N);
	populate_array(A);
	populate_array(B);

	double r1 = 0.0;
	double r2 = 0.0;

	struct timeval end, start;
	gettimeofday(&start, NULL);
	r1 = dot(A,B);
	gettimeofday(&end, NULL);
	uint64_t r1_time = (end.tv_usec - start.tv_usec);
	
	struct timeval end2, start2;
	gettimeofday(&start2, NULL);
	r2 = dot_parallel(A,B);
	gettimeofday(&end2, NULL);
	uint64_t r2_time = (end2.tv_usec - start2.tv_usec);

	printf("dot_seq --> %f (%" PRIu64 " usec)\n", r1, r1_time);
	printf("dot_par --> %f (%" PRIu64 " usec)\n", r2, r2_time);
}




