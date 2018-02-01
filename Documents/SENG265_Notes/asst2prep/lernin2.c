#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

	char *buffer = (char *) malloc(sizeof(char)*100);
	if (buffer==NULL){
		printf("ERROR\n");
		exit(1);
	}
	else{
		strncpy(buffer, "HEllo world", 12);//this works and the string literal approach did not because...
		//when you create a string literal, it is ALWAYS stored in the "data" portion of memory. I made buffer point to somewhere that was not in the heap! That's why running free caused problems!
		//Use strncpy to put strings into the heap! String literals won't do the job.

	//	buffer = "Did you ever hear the tragedy of Darth Plagueis the Wise?";
		printf("Hey!  %s\n", buffer);
		free(buffer);
	}
	exit(0);
}
