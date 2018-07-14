#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

	if (argc != 2) {
		return 1;
	}

	int x = atoi(argv[1]);

	printf("Hello World %d!\n", x);
	return 0;
}
