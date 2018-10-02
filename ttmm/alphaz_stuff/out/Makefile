CFLAGS= -O3 -I/usr/include/malloc/ 
VECFLAGS= -qopt-report=5 -qopt-report-phase=loop,vec -fma -xCORE-AVX-I 
LIBRARIES=-lm
CC=icc
OBJS = TMM.o 
all: plain check

debug: CFLAGS =-DDEBUG -g -Wall -Wextra -std=c99 -I/usr/include/malloc/
debug: all
		
plain: $(OBJS)
	$(CC) TMM-wrapper.c -o TMM $(OBJS) $(CFLAGS) $(LIBRARIES)

check: $(OBJS)
	$(CC) TMM-wrapper.c -o TMM.check $(OBJS) $(CFLAGS) $(LIBRARIES) -DCHECKING

verify: $(OBJS) TMM_verify.o
	$(CC) TMM-wrapper.c -o TMM.verify $(OBJS) TMM_verify.o $(CFLAGS) $(LIBRARIES) -DVERIFY

verify-rand: $(OBJS) TMM_verify.o
	$(CC) TMM-wrapper.c -o TMM.verify-rand $(OBJS) TMM_verify.o $(CFLAGS) $(LIBRARIES) -DVERIFY -DRANDOM

TMM.o : clean TMM.c
	$(CC) TMM.c -o TMM.o $(CFLAGS) $(LIBRARIES) -c $(VECFLAGS)

TMM_verify.o : TMM_verify.c
	$(CC) TMM_verify.c -o TMM_verify.o $(CFLAGS) $(LIBRARIES) -c

clean:
	rm -f *.o TMM TMM.check TMM.verify TMM.verify-rand
