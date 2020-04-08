#include <stdio.h>
#include <stdlib.h>

void Bracket_generate(int left,int right,char *str,char *result);

char** generateParenthesis(int n, int* returnSize);

int main()
{
    int n;
    int size;
    char **kuo;
    scanf("%d",&n);
    kuo = generateParenthesis(n,&size);
    for(int i = 0;i<size;i++){
        printf("%s\n",kuo[i]);
    }
    free(kuo);
    return 0;
}
char** generateParenthesis(int n, int* returnSize){
    char str[10000] = "\0";
    char *result;
    char ** ans;
    result = (char*)calloc(10000,sizeof(char));
    Bracket_generate(n,n,str,result);
    *returnSize = strlen(result)/(n*2);
    ans = (char **)calloc(*returnSize,sizeof(char *));
    ans[0] = (char *)calloc(10000,sizeof(char));
    int i,k = 0,j = 0;
    for(i = 0;i< (*returnSize)*n*2;i++){
        if(i % (n*2) == 0 && i!=0){
            ans[k][j] = '\0';
            k++;
            j = 0;
            ans[k] = (char *)calloc(10000,sizeof(char));
        }
        ans[k][j] = result[i];
        j++;
    }
    free(result);
    return ans;
}

void Bracket_generate(int left,int right,char *str,char *result){
    char str_temp[10000] = "\0";
    char str_temp1[10000] = "\0";
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
