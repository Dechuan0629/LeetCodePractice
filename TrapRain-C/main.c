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
    while(left<right){                                          //˫ָ�룬�����߿�ʼѰ��
        if(height[left] < height[right]){                       //����ָ��ָ��ĸ߶�С����ָ��ָ��ĸ߶ȣ���Ϊ����һ����ȡ����С��һ����ǽ�ĸ߶ȣ������м�һ�����Դ����ˮ����˶���ָ����и���
            if(height[left] >= leftmax) leftmax = height[left];
            else ans+=leftmax-height[left];                     //����ߵ�ǽ�ĸ߶ȼ�ȥ��ǰǽ�ĸ߶ȣ����Եõ���ǰλ�����ܴ�ŵ���ˮ������Ϊ��ǽ��ʱС����ǽ�����һ�����Խ��и��£�
            left++;
        }
        else{                                                   //��֮��ͬ
            if(height[right] >= rightmax) rightmax = height[right];
            else ans+=rightmax-height[right];
            right--;
        }
    }
    return ans;
}
