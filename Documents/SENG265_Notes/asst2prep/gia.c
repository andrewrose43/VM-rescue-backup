/*Growing integer array*/
#include <stdio.h>
#include <stdlib.h>

typedef struct int_struct{
	int *array;
	size_t used;
	size_t size;
}Int_Struct;

void initArray(Int_Struct *a, size_t initialSize){
	a->array = (int*)malloc(initialSize*sizeof(int));
	a->used = 0;
	a->size = initialSize;
}

void insertArray(Int_Struct *a, int element){
	//a->used is the number of used entries, because a->array[a->used++] updates a->used only *after* the array has been accessed
	//therefore a->used can go up to a->size
	if (a->used == a->size){
		a->size *=2;
		a->array = (int*)realloc(a->array, a->size*sizeof(int));
	}
	a->array[a->used++] = element;
}
/*Some notes on realloc
Realloc returns a void pointer to the new allocation! It "attempts to resize the memory block pointed to by ptr that was previouly allocated with a call to malloc or calloc.
void *realloc(void *ptr, size_t size);
Note that since realloc returns a void pointer, you need to cast its output! (int*)realloc(etc);
The input size is the size that you are resizing to.
*/

void freeArray(Int_Struct *a){
	free(a->array);//clear the memory
	a->array = NULL;//clear the pointer to the old memory block
	a->used = a->size = 0;
}

int main(){
Int_Struct a;
int i;

initArray(&a, 5); //initially 5 elements
for(i=0;i<100;i++) insertArray(&a, i); //automatically resizes as necessary

printf("%d\n", a.array[9]); //print 10th element
printf("%d\n", (int)a.used); //print number of elements
freeArray(&a);

}
