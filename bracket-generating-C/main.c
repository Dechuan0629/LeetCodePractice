#include <stdio.h>
#include <stdlib.h>

char Bracket_generate(int left,int right,char *str,char *result);

char* generateParenthesis(int n, int* returnSize);


int main()
{
    int n;
    int size;
    char *kuo;
    scanf("%d",&n);
    kuo = generateParenthesis(n,&size);
    printf("%s",kuo);
    return 0;
}

char* generateParenthesis(int n, int* returnSize){
    char str[100] = "\0";
    char *result;
    result = (char*)calloc(100,sizeof(char));
    Bracket_generate(n,n,str,result);
    result = result;
    *returnSize = strlen(result)/(n*2);
    return result;
}

char Bracket_generate(int left,int right,char *str,char *result){
    char str_temp[100] = "\0";
    char str_temp1[100] = "\0";
    strcpy(str_temp,str);
    strcpy(str_temp1,str);
    if (left > right) return;
    if(left ==0 && right == 0) strcat(result,str_temp);
    if(left>0)
    {
        str_temp[strlen(str_temp)] = '(';
        Bracket_generate(left-1,right,str_temp,result);

    }
    if(left<=right){
        str_temp1[strlen(str_temp1)] = ')';
        Bracket_generate(left,right-1,str_temp1,result);
    }
}
