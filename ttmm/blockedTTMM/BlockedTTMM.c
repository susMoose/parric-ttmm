//New BlockedTTMM
// Includes
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <mkl.h>


// Common Macros
#define max(x, y)   ((x)>(y) ? (x) : (y))
#define MAX(x, y)	((x)>(y) ? (x) : (y))
#define min(x, y)   ((x)>(y) ? (y) : (x))
#define MIN(x, y)	((x)>(y) ? (y) : (x))
#define CEILD(n,d)  (int)ceil(((double)(n))/((double)(d)))
#define ceild(n,d)  (int)ceil(((double)(n))/((double)(d)))
#define FLOORD(n,d) (int)floor(((double)(n))/((double)(d)))
#define floord(n,d) (int)floor(((double)(n))/((double)(d)))
#define CDIV(x,y)    CEILD((x),(y))
#define div(x,y)    CDIV((x),(y))
#define FDIV(x,y)    FLOORD((x),(y))
#define LB_SHIFT(b,s)  ((int)ceild(b,s) * s)
#define MOD(i,j)   ((i)%(j))
#define mallocCheck(v,s,d) if ((v) == NULL) { printf("Failed to allocate memory for %s : size=%lu\n", "sizeof(d)*(s)", sizeof(d)*(s)); exit(-1);}

void BlockedTTMM(long n, long b, float**** A, float**** B, float**** C){
    printf("\n Running BlockedTTMM \n");
    float a2dim[b][b];
    float b2dim[b][b];
    float c2dim[b][b];
    

    //c(i,k) += A(i,k)* B(k, J)
    int i, j, k, L; 
    
    for(i = 0; i < n; i++){
        for( j = 0; j<n; j++){
            for(k =0; k<n; k++){
                c[i][k] += A[i][k] * B[k][j];

            }
        }
    }
    
    
    
/*    
    
//a2dim[k][L] = A[i][j][k][L]
//b2dim[k][L] = B[i][j][k][L]

    for (i=0; i< n; i++) {                                   // for each row of big blocks
       for (j=0;j < n; j++) {                               //for each column of big blocks \
           printf("j: %d\n", j );
           int cur = 0;
           for (k=0;k < b; k++) {
               for (L=0; L<b; L++) {                //taking each inner block and assigning it temporarily to a 
                    cur = (i*n*b*b)+(j*b*b)+(k*b)+L;
                    
                    //printf("[%d] ", cur);
                    //printf("[%g] ", A[i][j][k][L]);
                }
                printf("\n");
            }
            printf("\n");
		}
        printf("\n");
    } //end of for loops */

}

