#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

	char *buffer = (char *) malloc(sizeof(char)*100);
	//I just made a pointer to a string that points somewhere in dynamic memory.
	if (buffer==NULL){
		printf("ERROR\n");
		exit(1);
	}
	else{
		buffer = "Did you ever hear the tragedy of Darth Plagueis the Wise?";
		printf("Hey!  %s\n", buffer);
		free(buffer);
	}
	exit(0);
}
