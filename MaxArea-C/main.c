#include <stdio.h>
#include <stdlib.h>


int main()
{
    int height[9] = {1,8,6,2,5,4,8,3,7};
    int ans = maxArea(height,9);
    printf("%d",ans);
    return 0;
}
//利用双指针，可将时间复杂度降为O（n）
int maxArea(int* height, int heightSize){  //面积大小应为 (x-y)*min(height[x],height[y])
    int pleft = 0,pright = heightSize-1;   //要保证取得最大的面积，那么满足的条件为x-y距离足够大，同时两边的最小高度要足够大
    int ans = 0;
    while(pleft < pright){                 //那么利用双指针从两边同时往中间走，我们在x-y在减小的同时，为了保证面积足够大，那么总是需要保存最高的边，因此对边较小的一个指针进行移动
        ans = ans > (pright-pleft)*(height[pleft] > height[pright] ? height[pright]:height[pleft]) ? ans:(pright-pleft)*(height[pleft] > height[pright] ? height[pright]:height[pleft]);
        if(height[pleft] > height[pright]) pright--;
        else pleft++;
    }
    return ans;
}

//暴力方法，时间复杂度为O（n^2），leetcode上C语言不会超时，python会超时
int maxArea1(int* height, int heightSize){
    int i,j,ans = 0;
    for(i=0;i<heightSize;i++){
        for(j=i;j<heightSize;j++){   //max(ans,(right-left)*min(height[left],height[right]))
            ans = ans > (j-i)*(height[i] > height[j] ? height[j]:height[i]) ? ans:(j-i)*(height[i] > height[j] ? height[j]:height[i]);
        }
    }
    return ans;
}
