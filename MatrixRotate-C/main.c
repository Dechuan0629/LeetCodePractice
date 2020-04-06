#include <stdio.h>
#include <stdlib.h>

int main()
{
    int matrix[4][4] = {{5, 1, 9, 11},
                        {2, 4, 8, 10},
                        {13, 3, 6, 7},
                        {15,14,12,16}};
    int *p[4],size = 4;
    p[0] = &matrix[0][0];
    p[1] = matrix[1];
    p[2] = matrix[2];
    p[3] = matrix[3];
    rotate(p,4,&size);
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
        {
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int i,j,temp_x,temp_y,temp1,temp2,x,y;
    for(i=0;i<(int)matrixSize/2;i++){             //控制旋转的是第几圈
        for(j=0;j<*matrixColSize-1-2*i;j++){        //控制当前圈需要旋转的个数
            x = i;
            y = j+i;
            temp2 = matrix[x][y];
            for(int k=0;k<4;k++){
                temp1 = temp2;
                temp_x = y;                                //当前值的坐标（x，y）旋转后的坐标值为（y，matrixSize-1-x)
                temp_y = matrixSize-1-x;
                temp2 = matrix[temp_x][temp_y];
                matrix[temp_x][temp_y] = temp1;
                x = temp_x;
                y = temp_y;

            }
        }
    }
}
