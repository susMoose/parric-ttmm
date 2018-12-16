// This file is generated from test alphabets program by code generator in alphaz
// To compile this code, use -lm option for math library.

// Includes
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <omp.h>
#include <immintrin.h>
#include <malloc.h>


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
#define mallocCheck(v,s,d) if ((v) == NULL) { printf("Failed to allocate memory for %s : size=%lu\n", "sizeof(d)*(s)", sizeof(d)*(s)); exit(-1); }
// Reduction Operators
#define RADD(x,y)    ((x)+=(y))
#define RMUL(x,y)    ((x)*=(y))
#define RMAX(x,y)    ((x)=MAX((x),(y)))
#define RMIN(x,y)    ((x)=MIN((x),(y)))

// Common functions for min and max
//functions for integer max
inline int __max_int(int x, int y){
	return ((x)>(y) ? (x) : (y));
}

inline short __max_short(short x, short y){
	return ((x)>(y) ? (x) : (y));
}

inline long __max_long(long x, long y){
	return ((x)>(y) ? (x) : (y));
}

inline unsigned int __max_unsigned_int(unsigned int x, unsigned int y){
	return ((x)>(y) ? (x) : (y));
}

inline unsigned short __max_unsigned_short(unsigned short x, unsigned short y){
	return ((x)>(y) ? (x) : (y));
}

//function for float max
inline float __max_float(float x, float y){
	return ((x)>(y) ? (x) : (y));
}

//function for double max
inline double __max_double(double x, double y){
	return ((x)>(y) ? (x) : (y));
}

//function for integer min
inline int __min_int(int x, int y){
	return ((x)>(y) ? (y) : (x));
}

inline short __min_short(short x, short y){
	return ((x)>(y) ? (y) : (x));
}

inline long __min_long(long x, long y){
	return ((x)>(y) ? (y) : (x));
}

inline unsigned int __min_unsigned_int(unsigned int x, unsigned int y){
	return ((x)>(y) ? (y) : (x));
}

inline unsigned short __min_unsigned_short(unsigned short x, unsigned short y){
	return ((x)>(y) ? (y) : (x));
}

inline unsigned long __min_unsigned_long(unsigned long x, unsigned long y){
	return ((x)>(y) ? (y) : (x));
}

inline float __min_float(float x, float y){
	return ((x)>(y) ? (y) : (x));
}

inline double __min_double(double x, double y){
	return ((x)>(y) ? (y) : (x));
}





//Memory Macros
#define A(i,j) A[i][j]
#define B(i,j) B[i][j]
#define R(i,j) R[i][j]

void TMM_verify(long N, long t1, long t2, long t3, float** A, float** B, float** R){
	///Parameter checking
	if (!((N >= 1))) {
		printf("The value of parameters are not valid.\n");
		exit(-1);
	}
	t1 += 1;
    t2 +=2;
    t3 +=3;
	//Memory Allocation
	
	#define S1(i,j,k) R(i,k) = (A(i,j))*(B(j,k))
	#define S2(i,j,k) R(i,k) = (R(i,k))+((A(i,j))*(B(j,k)))
	#define S0(i,j,i2) R(i,i2) = R(i,i2)
	{
		//Domain
		//{i,j,k|j==i && i>=1 && N>=k && k>=i && k>=1 && N>=i && N>=1}
		//{i,j,k|i>=1 && N>=k && k>=j && j>=i+1 && j>=2 && N>=j && k>=i && k>=1 && N>=1}
		//{i,j,i2|j==N && i2>=1 && N>=i2 && i>=1 && i2>=i && N>=1}
		int c1,c2,c3;
		for(c1=1;c1 <= N-2;c1+=1)
		 {
		 	for(c3=c1;c3 <= N;c3+=1)
		 	 {
		 	 	S1((c1),(c1),(c3));
		 	 }
		 	for(c2=c1+1;c2 <= N-1;c2+=1)
		 	 {
		 	 	for(c3=c2;c3 <= N;c3+=1)
		 	 	 {
		 	 	 	S2((c1),(c2),(c3));
		 	 	 }
		 	 }
		 	for(c3=c1;c3 <= N-1;c3+=1)
		 	 {
		 	 	S0((c1),(N),(c3));
		 	 }
		 	S2((c1),(N),(N));
		 	S0((c1),(N),(N));
		 }
		if ((N >= 2)) {
			{
				for(c3=N-1;c3 <= N;c3+=1)
				 {
				 	S1((N-1),(N-1),(c3));
				 }
				S0((N-1),(N),(N-1));
				S2((N-1),(N),(N));
				S0((N-1),(N),(N));
			}
		}
		S1((N),(N),(N));
		S0((N),(N),(N));
	}
	#undef S1
	#undef S2
	#undef S0
	
	//Memory Free
}

//Memory Macros
#undef A
#undef B
#undef R


//Common Macro undefs
#undef max
#undef MAX
#undef min
#undef MIN
#undef CEILD
#undef ceild
#undef FLOORD
#undef floord
#undef CDIV
#undef FDIV
#undef LB_SHIFT
#undef MOD
#undef RADD
#undef RMUL
#undef RMAX
#undef RMIN
