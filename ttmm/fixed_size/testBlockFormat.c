#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[]){
    float* base = (float*) malloc(TEST_SIZE*TEST_SIZE*sizeof(float));
    for(int i=0; i<TEST_SIZE*TEST_SIZE;i++)
        base[i]=i;
    for(int i=0;i<TEST_SIZE;i++){
        for(int j=0;j<TEST_SIZE;j++)
            printf("%3.0f ",base[TEST_SIZE*i+j]);
        printf("\n");
    }
    int new_size=0;
    float* newBase=toBlocks(base,TEST_SIZE, &new_size);
    printf("New size:%d.\n", new_size);
    for(int i=0;i<new_size;i++){
        for(int j=0;j<new_size;j++)
            printf("%3.0f ",newBase[new_size*i+j]);
        printf("\n");
    }
}
