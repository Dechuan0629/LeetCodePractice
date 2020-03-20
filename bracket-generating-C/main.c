#include <stdio.h>
#include <stdlib.h>

void Bracket_generate(int left,int right,char *str,char *result);

char* generateParenthesis(int n, int* returnSize);

int main()
{
    int n;
    int size;
    char *kuo;
    scanf("%d",&n);
    kuo = generateParenthesis(n,&size);
    for(int i = 0;i<size*n*2;i++){
        printf("%c",kuo[i]);
        if((i+1) % (n*2) == 0) printf("\n");
    }
    free(kuo);
    return 0;
}

char* generateParenthesis(int n, int* returnSize){
    char str[1000] = "\0";
    char *result;
    result = (char*)calloc(1000,sizeof(char));
    Bracket_generate(n,n,str,result);
    *returnSize = strlen(result)/(n*2);
    return result;
}

void Bracket_generate(int left,int right,char *str,char *result){
    char str_temp[1000] = "\0";
    char str_temp1[1000] = "\0";
    strcpy(str_temp,str);
    strcpy(str_temp1,str);
    if (left > right) return;          //当左括号的剩余数量大于右括号时，多出来的那个右括号将无法得到匹配，因此直接返回
    if(left ==0 && right == 0) strcat(result,str);
    if(left>0)                         //左括号可直接添加，右括号需要受到左括号数量的牵制
    {
        str_temp[strlen(str_temp)] = '(';
        Bracket_generate(left-1,right,str_temp,result);

    }
    if(left<right){                   //右括号的剩余数量大于左括号时，说明还有左括号没有得到匹配，因此可以进行添加
        str_temp1[strlen(str_temp1)] = ')';
        Bracket_generate(left,right-1,str_temp1,result);
    }
}
