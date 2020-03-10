#include <stdio.h>
#include <stdlib.h>

int sumNums(int num);

int main()
{
    int num = 0;
    printf("n = ");
    scanf("%d",&num);
    printf("%d",sumNums(num));
    return 0;
}

int sumNums(int num)
{
    if(num > 1) return num+=sumNums(num-1);
    else return 1;
}
