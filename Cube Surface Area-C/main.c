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
            ans += grid[i][j]*4+2;                             //单个立方体堆叠起来的面积公式为S=N*4+2
            if (i-1 >=0)
                ans -= min(grid[i][j],grid[i-1][j]);           //这个算法的做法是单独考虑每一个位点的正方体的重叠面积
            if (i+1 < gridSize)                             //当前位点的正方体如果与上下左右某个位置出现重合，便减去小的那个正方体的重合部分
                ans -= min(grid[i][j],grid[i+1][j]);          //也就是min（x，y）得到小的那个正方体，乘1
            if (j-1 >=0)                                   //加入判断条件防止边界上的正方体访问上下左右出现数组越界的情况
                ans -= min(grid[i][j],grid[i][j-1]);            //也可以去掉判断条件，在边界上扩充一圈0，i，j便从1开始
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
