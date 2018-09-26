CFLAGS= -Wall -Wextra -Wpedantic -Wfatal-errors -O3 -fopt-info-vec-all -ftree-vectorizer-verbose=0

all: add add_v
add: add.c
	gcc $< -o $@ $(CFLAGS)
add_v: add_v.c
	gcc -O3 $< -o $@ $(CFLAGS)
clean:
	rm -rf *.o add add_v

