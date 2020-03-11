#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num[8] = {10,9,2,5,3,7,101,18};
    int result = lengthOfLIS(num,8);
    printf("%d",result);
    return 0;
}

int lengthOfLIS(int* nums, int numsSize){
    int result=0;
    int *dp;
    int i,j;
    dp = (int*)calloc(numsSize,sizeof(int));
    for(i=0;i<numsSize;i++){
        for(j=0;j<i;j++){
            if(nums[i]>nums[j]){
                dp[i] = max(dp[i],dp[j]);
            }
        }
        dp[i]++;
        result = max(result,dp[i]);
    }
    free(dp);
    return result;
}


int max(int a, int b)
{
    if(a>b) return a;
    return b;
}
