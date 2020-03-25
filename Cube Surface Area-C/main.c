#include <stdio.h>
#include <stdlib.h>

int surfaceArea(int** grid, int gridSize, int* gridColSize);
int min(int a,int b);

int main()
{
    int grid[3][3] = {{2,2,2},{2,1,2},{2,2,2}};
    int *p[3];
    p[0] = &grid[0][0];
    p[1] = grid[1];
    p[2] = grid[2];
    int co = 3;
    int result = surfaceArea(p,3,&co);
    printf("Surface Area is : %d",result);
    return 0;
}

int surfaceArea(int** grid, int gridSize, int* gridColSize){
    int i,j,ans = 0;
    for(i=0;i<gridSize;i++){
        for(j=0;j<*gridColSize;j++){
            if(grid[i][j] == 0) continue;
            ans += grid[i][j]*4+2;                             //����������ѵ������������ʽΪS=N*4+2
            if (i-1 >=0)
                ans -= min(grid[i][j],grid[i-1][j]);           //����㷨�������ǵ�������ÿһ��λ�����������ص����
            if (i+1 < gridSize)                             //��ǰλ����������������������ĳ��λ�ó����غϣ����ȥС���Ǹ���������غϲ���
                ans -= min(grid[i][j],grid[i+1][j]);          //Ҳ����min��x��y���õ�С���Ǹ������壬��1
            if (j-1 >=0)                                   //�����ж�������ֹ�߽��ϵ�����������������ҳ�������Խ������
                ans -= min(grid[i][j],grid[i][j-1]);            //Ҳ����ȥ���ж��������ڱ߽�������һȦ0��i��j���1��ʼ
            if (j+1 < *gridColSize)
                ans -= min(grid[i][j],grid[i][j+1]);
        }
    }
    return ans;
}

int min(int a,int b){
    if(a>b) return b;
    else return a;
}
