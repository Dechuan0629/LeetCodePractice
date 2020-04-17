#include <stdio.h>
#include <stdlib.h>

int main()
{
    int height[12] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int res = trap(height,12);
    printf("%d",res);
    return 0;
}

int trap(int* height, int heightSize){
    int left = 0,right = heightSize-1,leftmax = 0,rightmax = 0;
    int ans = 0;
    while(left<right){                                          //双指针，从两边开始寻找
        if(height[left] < height[right]){                       //当左指针指向的高度小于右指针指向的高度，因为容量一定是取决于小的一方的墙的高度，所以中间一定可以存放雨水，因此对左指针进行更新
            if(height[left] >= leftmax) leftmax = height[left];
            else ans+=leftmax-height[left];                     //由最高的墙的高度减去当前墙的高度，可以得到当前位置所能存放的雨水量（因为左墙此时小于右墙，因此一定可以进行更新）
            left++;
        }
        else{                                                   //反之相同
            if(height[right] >= rightmax) rightmax = height[right];
            else ans+=rightmax-height[right];
            right--;
        }
    }
    return ans;
}
