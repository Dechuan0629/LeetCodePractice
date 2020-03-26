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

bool hasGroupsSizeX(int* deck, int deckSize){    //思路很简单，求出每个数字出现的次数，然后求出所有数字的次数的最大公约数
    int i,j = 0,size = deckSize/2;               //最大公约数即为可分为的分组，最大公约数大于等于二时，即可满足提议
    int count[100] = {0};
    int num[100] = {0};
    for(i=0;i<deckSize;i++){                     //得到每个数字出现的次数
        count[deck[i]]++;
    }
    for(i=0;i<100;i++){                          //将不为0次的数字放到前面
        if(count[i]!=0){
            num[j] = count[i];
            j++;
        }
    }
    int gcd_num = gcd(num[0],num[1]);
    for(i=2;i<100;i++){                          //得到所有次数的最大公约数
        if(num[i] == 0) break;
        gcd_num = gcd(gcd_num,num[i]);
    }
    if(gcd_num>=2) return true;
    else return false;
}

int gcd(int a,int b){                            //辗转相除法
    if(b==0) return a;
    else return gcd(b,a%b);
}
