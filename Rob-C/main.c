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
        ans = pre1 > pre2+nums[i] ? pre1:pre2+nums[i]; //pre1始终保存前面一个的值，pre2始终保存前面第二个的值，ans保存当前更新后的值，只有pre2可以加上当前值进行更新，比较大小即可
        pre2 = pre1;
        pre1 = ans;
    }
    return ans;
}
