#include <boost/numeric/ublas/matrix.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <chrono>

void TMM(long, float**, float**, float**);
using namespace std;

int main(int argc, char** argv){
	if(argc!=2){
		cerr<<"Use: "<<argv[0]<<" <N>\n";
		return 1;
	}
	srand(time(0));
	//read N from first argument
	long N;
	stringstream ss;
	ss<<argv[1];
	ss>>N;
	boost::numeric::ublas::matrix<float> A(N,N), B(N,N), C(N,N);
	//generate A randomly
	for(int i=0;i<N;i++){	
		for(int j=0;j<N;j++){
			A(i,j)=j<i?0:rand()%15;
		}
	}
	//generate B randomly
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				B(i,j)=j<i?0:rand()%15;
			}
		}
	//now make empty matrices in the format that alphaz expects
	float **a, **b, **c;
	a=new float*[N+1];
	for(int i=0;i<N+1;i++)
		a[i]=new float[N+1];
	b=new float*[N+1];
	for(int i=0;i<N+1;i++)
		b[i]=new float[N+1];
	c=new float*[N+1];
	for(int i=0;i<N+1;i++){
		c[i]=new float[N+1];
    }
	//now copy data from matrix A into array a
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			a[i+1][j+1]=A(i,j);
	//now copy data from matrix B into array b
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			b[i+1][j+1]=B(i,j);
	//now call the alphaz routine
	auto start= chrono::system_clock::now();
	TMM(N,a,b,c);
	auto end= chrono::system_clock::now();
	chrono::duration<double> elapsed_seconds = end-start;

	
	//now copy c into C, multiply A and B, and verify that the result is approximately C
	for(int i=0; i<N;i++){
		for(int j=i;j<N;j++){
			C(i,j)=c[i+1][j+1];
		}
	}
	boost::numeric::ublas::matrix<float> result=prod(A,B);
	
	for(int i=0;i<N;i++)
		for(int j=i;j<N;j++){
			if (abs(C(i,j)-result(i,j)) > .01)
				cerr<<"result at ("<<i<<", "<<j<<") was "<<result(i,j)<<" instead of "<<A(i,j)<<".\n";
		}
	cout<<"Alphaz time: "<<elapsed_seconds.count()<<"\n";
	return 0;
}
