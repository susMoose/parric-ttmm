#include <stdlib.h>
#include <stdio.h>
float* toBlocks(float *array, int sideLength, int* newSideLength){
    int blocksPerSide=sideLength/SIZE + ((sideLength% SIZE ==0)? 0:1);
    float* newArray= (float*)malloc(SIZE*SIZE*blocksPerSide*blocksPerSide*sizeof(float));
    *newSideLength=SIZE*blocksPerSide;
    //copy panel by panel
    int newArrayIndex=0;
    for(int blockI=0;blockI<blocksPerSide;blockI++)
    for(int blockJ=0;blockJ<blocksPerSide;blockJ++)
        for(int i=0;i<SIZE;i++){
            int arrayI=i+blockI*SIZE;
            for(int j=0;j<SIZE;j++){
                int arrayJ=j+blockJ*SIZE;
                newArray[newArrayIndex++]=( (arrayI<sideLength) && (arrayJ<sideLength) )? array[arrayI*sideLength+arrayJ]:0;
            }
        }
    return newArray;
}

void fromBlocks(float *blockmajor, float *normal, int bmsize, int nsize){
    int blocksPerSide=bmsize/SIZE;
    int bmArrayIndex=0;
    for(int blockI=0;blockI<blocksPerSide;blockI++)
    for(int blockJ=0;blockJ<blocksPerSide;blockJ++)
        for(int i=0;i<SIZE;i++){
            int arrayI=i+blockI*SIZE;
            for(int j=0;j<SIZE;j++){
                int arrayJ=j+blockJ*SIZE;
                if( (arrayI < nsize) && (arrayJ < nsize) )
                    normal[arrayI*nsize + arrayJ]=blockmajor[bmArrayIndex];
                bmArrayIndex+=1;
            }
        }
}
