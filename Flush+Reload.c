#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <memory.h>
#include <sys/mman.h>
#include <errno.h>
#include <sched.h>

#include "cacheutils.h"

#define _4KB 4096
#define LOOP 10000

static char __attribute__((aligned(4096))) probe_arr[256*4096];

size_t res[256];

int main(int argc, char *argv[]) {
	
	printf("- Detection flush_reload_theshold:%d\n",(int)detect_flush_reload_threshold());

        memset(probe_arr, 0x0, sizeof(probe_arr));
        memset(res, 0x0, sizeof(res));
        
	int target_number = atoi(argv[1]);

        for(int j=0; j<LOOP; j++){
                for(int i=0; i<256; i++)
                        flush(probe_arr + i*_4KB);

                maccess(probe_arr + target_number*_4KB);

                for(int i=0; i<256; i++)
                        res[i]+=reload_t(probe_arr + i*_4KB);
        }

        for(int i=0; i<256; i++)
                printf("%d: %d\n", i, (int)(res[i]/LOOP));
}                                
