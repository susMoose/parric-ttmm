#include <stdio.h>
#include <stdlib.h>

#define N 10

void add_v(double * restrict A, double * restrict B) {
	double *AA = __builtin_assume_aligned(A,16);
	double *BB = __builtin_assume_aligned(B,16);
	for (int i=0; i<N; i++) {
		AA[i] += BB[i];
	}
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
	add_v(A,B);
	//printf("I still compile.\n");
}
