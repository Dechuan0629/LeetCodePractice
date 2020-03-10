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
    for(i=0;i<numsSize;i++){         //���������������ʣ�1.�����ɣ�2.����ͬ�����Ϊ��,3.�κ�����0�����ڱ��������������е�������һ�������������ڽ��������ظ���������һ����������
        num^=nums[i];                //1^2^1^3^2^5 => 1^1^2^2^3^5 => 0^0^3^5 => 3^5
    }                                //������ͬ��������������Ϊ��ͬλ��Ϊ�㣬��ͬλΪ1����˵õ��Ľ���ķ���λ��Ӧ��������һ��Ϊ0��һ��Ϊ1�������ҵ�����������

    num = num & (~num + 1);          //num��num�ķ���+1��and�������õ����λΪ1��Ӧ����
    for(i=0;i<numsSize;i++){
        if(nums[i] & num) num1[0] ^= nums[i];          //��1�Ķ�Ӧλ����0��1��Ϊ���ѣ��ٴ��������������ȥ��ͬ������ԭ��������µľ����Ǹ���ͬ��������
        else num1[1] ^= nums[i];
    }
    *returnSize = 2;
    return num1;
}
