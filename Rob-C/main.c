#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[5] = {2,7,9,3,1};
    int res = rob(nums,5);
    printf("%d",res);
    return 0;
}

int rob(int* nums, int numsSize){
    int pre1 = 0,pre2 = 0,ans = 0;
    for(int i=0;i<numsSize;i++){
        ans = pre1 > pre2+nums[i] ? pre1:pre2+nums[i]; //pre1ʼ�ձ���ǰ��һ����ֵ��pre2ʼ�ձ���ǰ��ڶ�����ֵ��ans���浱ǰ���º��ֵ��ֻ��pre2���Լ��ϵ�ǰֵ���и��£��Ƚϴ�С����
        pre2 = pre1;
        pre1 = ans;
    }
    return ans;
}
