#include <stdio.h>
#include <stdlib.h>

int bestSeqAtIndex(int* height, int heightSize, int* weight, int weightSize);
int max(int a, int b);

/*结果能够AC，但是利用dp算法寻找最长上升子序列会超时*/

int main()
{
    int height[6] = {65,70,56,75,65,68};
    int weight[6] = {100,150,90,190,95,110};
    int result = 0;
    result = bestSeqAtIndex(height,6,weight,6);
    printf("%d",result);
    return 0;
}

int bestSeqAtIndex(int* height, int heightSize, int* weight, int weightSize){

    int people[2][heightSize];
    int i,j,temp1;
    int *p[2];
    memcpy(people[0],height,heightSize*sizeof(int));
    memcpy(people[1],weight,weightSize*sizeof(int));

    p[0] = &people[0][0];
    p[1] = people[1];
    quickSort(p,0,heightSize-1);

    for (i=0;i<2;i++){
        for(j=0;j<heightSize;j++){
            printf("%d ",people[i][j]);
        }
        printf("\n");
    }

    int result=0;
    int *dp;
    dp = (int*)calloc(heightSize,sizeof(int));

    for(i=0;i<heightSize;i++){
        for(j=0;j<i;j++){
            if(people[1][i]>people[1][j] && people[0][i]>people[0][j]){
                dp[i] = max(dp[i],dp[j]);
            }

        }
        dp[i]++;
        result = max(result,dp[i]);
    }
    free(dp);
    return result;
}

int max(int a, int b)
{
    if(a>b) return a;
    return b;
}

void quickSort(int **a,int left,int right)
{

    int i,j,temp,temp1;
    i=left;
    j=right;
    temp=a[0][left];
    temp1=a[1][left];
    if(left>right)
        return;
    while(i!=j)
    {
        while(a[0][j]>=temp && j>i)
            j--;
        if(j>i){
            a[1][i]=a[1][j];
            a[0][i++]=a[0][j];

        }

        while(a[0][i] <=temp && j>i)
            i++;
        if(j>i){
            a[1][j]=a[1][i];
            a[0][j--]=a[0][i];

        }

    }
    a[0][i]=temp;
    a[1][i]=temp1;
    quickSort(a,left,i-1);
    quickSort(a,i+1,right);
}
