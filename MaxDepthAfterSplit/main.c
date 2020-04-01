#include <stdio.h>
#include <stdlib.h>

int* maxDepthAfterSplit(char * seq, int* returnSize);

int main()
{
    char seq[100] = "(()())";
    int Size = 0;
    int *result = maxDepthAfterSplit(seq,&Size);
    for(int i=0;i<Size;i++){
        printf("%d ",result[i]);
    }
    free(result);
    return 0;
}

int* maxDepthAfterSplit(char * seq, int* returnSize){       //不需要用栈进行括号匹配，因为根据题意传入函数的序列已经是合法的括号序列了
    *returnSize = strlen(seq);
    int *ans = (int *)malloc(sizeof(int)*strlen(seq));
    for(int i=0;i<*returnSize;i++){                         //处于连续位置上的 ‘（’会增加括号的深度,也就是说处于连续位置上的左括号下标的奇偶性必定不同
        if ((seq[i] == '(' && i%2 ==0) || (seq[i] == ')' && (i+1)%2 == 0)){ //那么只需要将序列中，所有处于偶数位置的左括号分给A，所有处于奇数位置的左括号分给B，则必定可以保证深度不会增加
            ans[i] = 0;                                 //这时，当左括号位置是偶数时，则下一个奇数位的右括号必定与其匹配，反之同样满足
        }
        else ans[i] = 1;
    }
    return ans;
}
