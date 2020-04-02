#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//这道题我只想说写测试用例的大哥太强了，面向测试用例的编程

int myAtoi(char * str);
long long myPow(int i,int j);

int main()
{
    char num[100] = "  0000000000012345678";
    int ans = myAtoi(num);
    printf("%d",ans);
    return 0;
}

int myAtoi(char * str){
    int i = 0,judge = 0;
    long long number = 0;
    char temp = '\0';
    while(*(str+i) != '\0'){
        if( *(str+i) == ' ' && i == 0 && temp == '\0' && judge == 0){
            str = str+1;
            continue;
        }
        else if( (*(str+i) == '-' || *(str+i) == '+') && i == 0 && temp == '\0' && judge == 0){
             temp = *(str+i);
             str = str+1;
             continue;
        }
        else if( *(str+i) >= 48 && *(str+i) <= 57){
            if( *(str+i) == 48 && i == 0){
                str = str+1;
                judge = 1;
                continue;
            }
            i++;
        }
        else{
            *(str+i) = '\0';
            break;
        }
    }
    if(strlen(str) == 0) return 0;
    if(strlen(str)>10){
        if(temp == '-') return -2147483648;
        return 2147483647;
    }
    for(i=0;i<strlen(str);i++){
        if(str[i] == '0') continue;
        number += (str[i]-48) * myPow(10,strlen(str)-i-1);
    }
    if(number < -2147483648 || number > 2147483647){
        if(temp == '-') return -2147483648;
        return 2147483647;
    }
    if(temp == '-') return ~number+1;
    return number;
}

long long myPow(int i,int j){
    long long res = 1;
    for(int k=0;k<j;k++){
        res*=i;
    }
    return res;
}
