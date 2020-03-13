#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*LeetCode上调试了半天，一直在报AddressSanitizer，数组越界的错误，print了一下ASize才发现，测试用例原来根本没往函数里传递数组大小，C语言GG*/

int main()
{
    int num[5] = {17,85,93,-45,-21};
    int k = 140;
    int result=shortestSubarray(num,5,k);
    printf("%d",result);
    return 0;
}

int shortestSubarray(int* A, int ASize, int K){
    int i,j,temp=0,temp1= 0,min = -1,judge = 0;
    printf("%d\n",ASize);
    int sum[2][ASize+1];
    int *p[2];
    sum[0][0] = 0;
    sum[1][0] = 0;
    for(i=0;i<ASize;i++){
        temp+=A[i];
        sum[0][i+1] = i+1;
        sum[1][i+1] = temp;
    }
    p[0] = &sum[0][0];
    p[1] = sum[1];
    quickSort(p,0,ASize);

    for(i=0;i<2;i++){
        for(j=0;j<=ASize;j++) printf("%d ",sum[i][j]);
        printf("\n");
    }
    for(i=0;i<=ASize;i++){
        if(sum[1][ASize]-sum[1][i]>=K){
            temp1 = sum[0][ASize]-sum[0][i];
        }
        else break;
        if(min > temp1 || i==0) min = temp1;
    }
    return min;
}

void quickSort(int **a,int left,int right)
{
    int i,j,temp,temp1;
    i=left;
    j=right;
    temp=a[1][left];
    temp1=a[0][left];
    if(left>right)
        return;
    while(i!=j)
    {
        while(a[1][j]>=temp && j>i)
            j--;
        if(j>i){
            a[0][i]=a[0][j];
            a[1][i]=a[1][j];
            i++;

        }

        while(a[1][i] <=temp && j>i)
            i++;
        if(j>i){
            a[0][j]=a[0][i];
            a[1][j--]=a[1][i];

        }
    }
    a[1][i]=temp;
    a[0][i]=temp1;
    quickSort(a,left,j-1);
    quickSort(a,i+1,right);
}


