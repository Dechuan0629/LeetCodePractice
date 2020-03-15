#include <stdio.h>
#include <stdlib.h>
/*会超时，难受。思考过后感觉不应该传链表进去添加，会严重的受到先朝右走还是先朝下走的影响，还是应该直接传入数组进行添加回溯*/
/*dfs应改为传入二维数组和行数记录*/
/*改为int dfs(int **grid, int i,int j,int row_size,int column_size, int **result, int idx, int *returnSize)*/

int** pathWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize, int* returnSize, int** returnColumnSizes);

typedef struct node{
    int x;
    int y;
    struct node *next;
}Node;

int main()
{
    int num[3][3] = {{0,0,0},{0,1,0},{0,0,0}};
    int *p[3],size = 3;
    p[0] = &num[0][0];
    p[1] = num[1];
    p[2] = num[2];
    int returnSize,*returnColumnSizes;
    int **result = pathWithObstacles(p,3,&size,&returnSize,&returnColumnSizes);
    int i,j;
    for(i=0;i<returnSize;i++){
        for(j=0;j<*returnColumnSizes;j++){
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }
    return 0;
}

int** pathWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize, int* returnSize, int** returnColumnSizes){
    int row = obstacleGridSize;
    int column = obstacleGridColSize[0];
    int **res = (int**)malloc(sizeof(int*) * row * column);
    Node *head,*p;
    int **result = (int **)malloc(sizeof(int *) * 1);
    int i=0;
    head = (Node *)calloc(1,sizeof(Node));
    dfs(obstacleGrid,0,0,row,column,head);
    p = head;
    *returnColumnSizes = (int*)malloc(sizeof(int) * row * column);
    while(p->next!=NULL){
        if(i>0) result = (int **)realloc(result,sizeof(int *) * (i+1));
        *(result+i) = (int *)calloc(2,sizeof(int));
        result[i][0] = p->x;
        result[i][1] = p->y;
        p = p->next;
        (*returnColumnSizes)[i] = 2;
        i++;
    }
    *returnSize = i;
    if(row==1 && column==1 && obstacleGrid[0][0]==1){
        *returnSize = 0;
        return res;
    }
    if((i==1 && row>1) || (i>1 && (result[i-1][0]!=row-1 || result[i-1][1]!=column-1))){
        *returnSize = 0;
        return res;
    }
    return result;
}

int dfs(int** grid,int i,int j,int row_size,int column_size,Node *p){   //利用深度优先对岛屿范围进行搜索
    if(i<0 || j<0 || i>=row_size || j>=column_size || grid[i][j]==1){   //到边界了或者是遇到障碍物了返回
        p = NULL;
        free(p);
        return 0;
    }
    if((j!=column_size-1 && i==row_size-1 && grid[i][j+1] == 1) || (i!=row_size-1 && j==column_size-1 && grid[i+1][j]==1)){  //到边界了，同时下方或者右方有障碍物，对这个值不记录。
        p = NULL;
        free(p);
        return 0;
    }
    Node *p1;
    p1 = (Node *)calloc(1,sizeof(Node));
    p->next = p1;
    p->x = i;
    p->y = j;
    p1->next = NULL;
    int num = 1;
    num = dfs(grid,i,j+1,row_size,column_size,p1); //向下探索
    num = dfs(grid,i+1,j,row_size,column_size,p1); //向右探索

    return num;
}
