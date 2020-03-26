#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool hasGroupsSizeX(int* deck, int deckSize);
int gcd(int a,int b);

int main()
{
    int cards[50] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,5,6,6,7,8,9,10};
    printf("%d",hasGroupsSizeX(cards,50));
    return 0;
}

bool hasGroupsSizeX(int* deck, int deckSize){    //˼·�ܼ򵥣����ÿ�����ֳ��ֵĴ�����Ȼ������������ֵĴ��������Լ��
    int i,j = 0,size = deckSize/2;               //���Լ����Ϊ�ɷ�Ϊ�ķ��飬���Լ�����ڵ��ڶ�ʱ��������������
    int count[100] = {0};
    int num[100] = {0};
    for(i=0;i<deckSize;i++){                     //�õ�ÿ�����ֳ��ֵĴ���
        count[deck[i]]++;
    }
    for(i=0;i<100;i++){                          //����Ϊ0�ε����ַŵ�ǰ��
        if(count[i]!=0){
            num[j] = count[i];
            j++;
        }
    }
    int gcd_num = gcd(num[0],num[1]);
    for(i=2;i<100;i++){                          //�õ����д��������Լ��
        if(num[i] == 0) break;
        gcd_num = gcd(gcd_num,num[i]);
    }
    if(gcd_num>=2) return true;
    else return false;
}

int gcd(int a,int b){                            //շת�����
    if(b==0) return a;
    else return gcd(b,a%b);
}
