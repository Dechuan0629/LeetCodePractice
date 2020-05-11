#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[6] = {7,3,1,5,21,9};
    int ans = maxProfit(nums,6);
    printf("%d",ans);
    return 0;
}

int maxProfit(int* prices, int pricesSize){   //ʱ�临�Ӷ�O(n)���ռ临�Ӷ�O(1)
    if (pricesSize == 0) return 0;
    int min_num = prices[0],ans = 0;
    for(int i=1;i<pricesSize;i++){
        ans = (prices[i] - min_num) > ans ? (prices[i] - min_num) : ans;   //��������ֵ
        min_num = min_num < prices[i] ? min_num : prices[i];    //����ǰ����С��ֵ
    }
    return ans;
}
