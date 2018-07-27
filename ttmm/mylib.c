#include <stdio.h>
#include <stdlib.h>

int multiply(int, int);
int multiply3(int, int, int);

int main(int argc, char** argv) {
	int x = atoi(argv[1]);
	int y = atoi(argv[2]);
	printf("%d * %d = %d\n (ttmm-0)", x, y, multiply(x,y));
	// another comment here
	return 0;
}
// hooorrayyy
int multiply(int x, int y) {
	int a = x;
	int b = y;
	return a*b;
}

int multiply3(int x, int y, int z) {
	// lorem ipsum sit dolor amet 
	return multiply(x,y)*z;
}
