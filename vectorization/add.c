#include <stdio.h>
#include <stdlib.h>

#define N 10

void add(double *A, double *B) {
    for (int i=0; i<N; i++) {
        A[i] += B[i];
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
	add(A,B);
	printf("I still compile.\n");
}
