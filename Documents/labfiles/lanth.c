#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
	/*
	char* str = "All you can upgrade is lanth?!";
	int len = strlen(str);
	printf("Lanth of string: %d\n", len);
*/
	
	char infile[100];
	char *arg = "--infile"; //so if you call the program with this option, it does funky shit with it!
	
	int len;
	for (int i = 0; i < argc; ++i){
		printf("%s\n", argv[i]);
		len = strlen(argv[i]);
		printf("\t%d\n", len);
		//backslash t adds a TAB to the print!

		if (!strcmp(arg, argv[i])) { //strcmp returns 0 if they are equal, -1 if less than, 1 if greater than
			printf("\tinfile switch found\n\n");
			strncpy(infile, argv[i+1], strlen(argv[i+1])+1);
		}
	}
	
	printf("Copied command: %s\n", infile);
	
	//lab4 --infile textfile.txt --sort
	//this might be how you make your code take a file rather than regular input

	return 0;
}
