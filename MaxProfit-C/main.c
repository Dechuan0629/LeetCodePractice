#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[6] = {7,3,1,5,21,9};
    int ans = maxProfit(nums,6);
    printf("%d",ans);
    return 0;
}

int maxProfit(int* prices, int pricesSize){   //时间复杂度O(n)，空间复杂度O(1)
    if (pricesSize == 0) return 0;
    int min_num = prices[0],ans = 0;
    for(int i=1;i<pricesSize;i++){
        ans = (prices[i] - min_num) > ans ? (prices[i] - min_num) : ans;   //保存最大差值
        min_num = min_num < prices[i] ? min_num : prices[i];    //保存前面最小的值
    }
    return ans;
}
