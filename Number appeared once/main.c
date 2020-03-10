#include <stdio.h>
#include <stdlib.h>

int* singleNumber(int* nums, int numsSize, int* returnSize);


int main()
{
    int *num,*num1,n;
    int size = 0,i;
    printf("please input how many numbers you want:");
    scanf("%d",&n);
    num = (int *)calloc(n,sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",num+i);
    }
    num1 = singleNumber(num,n,&size);
    printf("the single number is:%d,%d",num1[0],num1[1]);
    free(num);
    free(num1);
    return 0;
}

int* singleNumber(int* nums, int numsSize, int* returnSize){
    int num = 0,i,*num1;
    num1 = (int*)calloc(2,sizeof(int));
    for(i=0;i<numsSize;i++){         //利用异或操作的性质：1.交换律，2.两相同数异或为零,3.任何数与0异或等于本身。对数组里所有的数进行一次异或操作，等于将两个不重复的数进行一次异或操作。
        num^=nums[i];                //1^2^1^3^2^5 => 1^1^2^2^3^5 => 0^0^3^5 => 3^5
    }                                //两个不同的数进行异或后，因为相同位变为零，不同位为1，因此得到的结果的非零位对应的两数，一个为0，一个为1，即可找到单独的两数

    num = num & (~num + 1);          //num与num的反码+1做and操作，得到最低位为1对应的数
    for(i=0;i<numsSize;i++){
        if(nums[i] & num) num1[0] ^= nums[i];          //将1的对应位，按0和1分为两堆，再次利用两数异或消去相同的数的原理，最后留下的就是那个不同的数本身
        else num1[1] ^= nums[i];
    }
    *returnSize = 2;
    return num1;
}
