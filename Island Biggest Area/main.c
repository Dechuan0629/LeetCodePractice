#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num[4][5] = {{1,1,0,0,0},{1,1,0,0,0},{0,0,0,1,1},{0,0,0,1,1}};
    int *p[4];
    p[0] = &num[0][0];
    p[1] = num[1];
    p[2] = num[2];
    p[3] = num[3];
    int size = 5;
    int result = maxAreaOfIsland(p,4,&size);
    printf("%d",result);
    return 0;
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    int max_num=0;
    printf("%d,%d\n",gridSize,*gridColSize);
    int i,j;
    for(i=0;i<gridSize;i++){
        for(j=0;j<*gridColSize;j++){
            if(grid[i][j] == 1){
                max_num = max(max_num,dfs(grid,i,j,gridSize,*gridColSize));
            }
        }
    }
    free(grid);
    return max_num;
}

int dfs(int** grid,int i,int j,int row_size,int column_size){   //����������ȶԵ��췶Χ��������
    if(i<0 || j<0 || i>=row_size || j>=column_size || grid[i][j]==0)   //���ȷ�ֹ����Խ�磬Ȼ��������Ϊ0��ֵ����ֹ������
        return 0;
    grid[i][j] = 0;                  //��Ϊ��Ҫ�����ĵ�������ͨ��������˶����������ĵ�����0����ֹ�ظ�������
    int num = 1;
    num+=dfs(grid,i-1,j,row_size,column_size); //����̽��
    num+=dfs(grid,i+1,j,row_size,column_size); //����̽��
    num+=dfs(grid,i,j-1,row_size,column_size); //����̽��
    num+=dfs(grid,i,j+1,row_size,column_size); //����̽��

    return num;
}

int max(int a,int b){
    if(a>b) return a;
    else return b;
}
