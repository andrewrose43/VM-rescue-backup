#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
	printf("%d\n", argc);
	for (int i = 0; i <argc-1; i++){
		printf("%s\n", *++argv);
	}
		return 0;
}
