mylib.o: mylib.c
	gcc -c mylib.c

mylib: mylib.o
	gcc mylib.o -o mylib

all: mylib

clean:
	rm -rf mylib.o mylib
