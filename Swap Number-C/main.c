#include <stdio.h>
#include <stdlib.h>

int* swapNumbers(int* numbers, int numbersSize, int* returnSize);

int main()
{
    int num[2],size = 0;
    for(int i = 0;i<2;i++){
        scanf("%d",&num[i]);
    }
    swapNumbers(num,2,&size);
    return 0;
}

int* swapNumbers(int* numbers, int numbersSize, int* returnSize){
    numbers[0] = numbers[0] ^ numbers[1];
    numbers[1] = numbers[1] ^ numbers[0];
    numbers[0] = numbers[0] ^ numbers[1];
    *returnSize = numbersSize;
    return numbers;
}
