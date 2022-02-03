all: spy victim 

spy: spy.c
	gcc -std=gnu11 -O3 -o $@ $@.c

victim: victim.c
	gcc -std=gnu11 -O3 -o $@ $@.c

clean:
	rm spy victim
