#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

	int *a = malloc(sizeof(int));
	//I just made a pointer to an int that points somewhere in dynamic memory.
	if (a==NULL){
		printf("ERROR\n");
		exit(1);
	}
	*a = 5;
	printf("The value of a is %d\n", *a);

}
