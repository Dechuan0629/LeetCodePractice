#include <stdio.h>
#include <stdlib.h>


int main()
{
    int height[9] = {1,8,6,2,5,4,8,3,7};
    int ans = maxArea(height,9);
    printf("%d",ans);
    return 0;
}
//����˫ָ�룬�ɽ�ʱ�临�ӶȽ�ΪO��n��
int maxArea(int* height, int heightSize){  //�����СӦΪ (x-y)*min(height[x],height[y])
    int pleft = 0,pright = heightSize-1;   //Ҫ��֤ȡ�������������ô���������Ϊx-y�����㹻��ͬʱ���ߵ���С�߶�Ҫ�㹻��
    int ans = 0;
    while(pleft < pright){                 //��ô����˫ָ�������ͬʱ���м��ߣ�������x-y�ڼ�С��ͬʱ��Ϊ�˱�֤����㹻����ô������Ҫ������ߵıߣ���˶Ա߽�С��һ��ָ������ƶ�
        ans = ans > (pright-pleft)*(height[pleft] > height[pright] ? height[pright]:height[pleft]) ? ans:(pright-pleft)*(height[pleft] > height[pright] ? height[pright]:height[pleft]);
        if(height[pleft] > height[pright]) pright--;
        else pleft++;
    }
    return ans;
}

//����������ʱ�临�Ӷ�ΪO��n^2����leetcode��C���Բ��ᳬʱ��python�ᳬʱ
int maxArea1(int* height, int heightSize){
    int i,j,ans = 0;
    for(i=0;i<heightSize;i++){
        for(j=i;j<heightSize;j++){   //max(ans,(right-left)*min(height[left],height[right]))
            ans = ans > (j-i)*(height[i] > height[j] ? height[j]:height[i]) ? ans:(j-i)*(height[i] > height[j] ? height[j]:height[i]);
        }
    }
    return ans;
}
