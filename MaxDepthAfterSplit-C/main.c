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

int* maxDepthAfterSplit(char * seq, int* returnSize){       //����Ҫ��ջ��������ƥ�䣬��Ϊ�������⴫�뺯���������Ѿ��ǺϷ�������������
    *returnSize = strlen(seq);
    int *ans = (int *)malloc(sizeof(int)*strlen(seq));
    for(int i=0;i<*returnSize;i++){                         //��������λ���ϵ� ���������������ŵ����,Ҳ����˵��������λ���ϵ��������±����ż�Աض���ͬ
        if ((seq[i] == '(' && i%2 ==0) || (seq[i] == ')' && (i+1)%2 == 0)){ //��ôֻ��Ҫ�������У����д���ż��λ�õ������ŷָ�A�����д�������λ�õ������ŷָ�B����ض����Ա�֤��Ȳ�������
            ans[i] = 0;                                 //��ʱ����������λ����ż��ʱ������һ������λ�������űض�����ƥ�䣬��֮ͬ������
        }
        else ans[i] = 1;
    }
    return ans;
}
