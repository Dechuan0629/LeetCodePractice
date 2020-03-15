#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool canThreePartsEqualSum(int* A, int ASize);

int main()
{
    int num[4] = {1,-1,1,-1};
    //num = (int *)calloc(10,sizeof(int));
    if(canThreePartsEqualSum(num,4)){
        printf("true");
    }
    else printf("false");
    return 0;
}

bool canThreePartsEqualSum(int* A, int ASize){
    int i,sum = 0,num = 0,count = 0,sum1= 0;
    for(i=0;i<ASize;i++){
        sum+=A[i];
    }
    if(sum%3!=0) return false;                //因为要分为三部分，所以首要条件三个部分的和相加必定为3的倍数
    num = sum/3;                              //观察后可发现，三部分分别的和为总和除以3
    sum = 0;
    for(i=0;i<ASize;i++){
        sum+=A[i];
        if(count==3){                         //当已经分出三部分后，如果后面的数相加不为0，则为错误分组
            sum1+=A[i];
            if(i == ASize-1){
                if(sum1!=0){
                    count+=1;
                }
            }
            continue;
        }

        if(sum==num){
            count+=1;
            sum = 0;
        }
    }
    if(count==3) return true;
    else return false;
}
