#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Compile-time constants
#define MAX_WORD_LEN 20
#define MAX_WORDS 100
#define MAX_LINE_LEN 100
#define MAX_LINES 10

//Global variables
int num_words = 0;
int num_lines = 0;
char lines[MAX_LINES][MAX_LINE_LEN];
char words[MAX_WORDS][MAX_WORD_LEN];//note that the dimensions of the arrays are not stored with the arrays!
//this is C, not Java!
 
void dump_words (void);
void tokenize_line (char *); //function declarations

void dump_words(){
	int i = 0;
	for (i = 0; i<num_words; i++){
		printf("%5d : %s\n", i, words[i]);
	}
	return;
}

void tokenize_line(char *input_line){
	char *t;
	printf("Input line, as received by tokenize_line: %s\n", input_line);
	t = strtok(input_line, " ");
	//in the next line, that t in the loop condition counts as true so long as t exists (so long as we have not run out of tokens)
	while(t && num_words < MAX_WORDS){
		strncpy(words[num_words], t, MAX_WORD_LEN);
		num_words++;
		t = strtok(NULL, " ");
	}
	return;
}


int main(int argc, char *argv[]){ //recall that every separate input is a line!
	int i;
	
	if (argc==1) exit(0);

	for (i=0; i<argc-1; i++){
		strncpy(lines[i], argv[i+1], MAX_LINE_LEN);
		tokenize_line(lines[i]);
	}

	dump_words();

	printf("first line: \"%s\"\n", lines[0]);

	exit(0);
}
