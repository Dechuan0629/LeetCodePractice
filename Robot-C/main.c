#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//����ܹ�AC�����ǻᳬʱ T T
bool robot(char * command, int** obstacles, int obstaclesSize, int* obstaclesColSize, int x, int y);

int main()
{
    char command[100] = "RRUUUUUU";
    printf("%d",0&0)
    printf("%d",strlen(command));
    int ob[7][2];
    int *p[7];
    for(int i=0;i<7;i++)
        for(int j=0;j<2;j++) scanf("%d",&ob[i][j]);
    p[0] = &ob[0][0];
    p[1] = ob[1];
    p[2] = ob[2];
    p[3] = ob[3];
    p[4] = ob[4];
    p[5] = ob[5];
    p[6] = ob[6];
    if(robot(command,p,7,NULL,771,7174))printf("true");
    else printf("false");
    return 0;
}

bool robot(char * command, int** obstacles, int obstaclesSize, int* obstaclesColSize, int x, int y){  //obstacles��һά�����м����ϰ���ڶ�ά�±�0����x���꣬�±�1����y����
    int step[1][2],count=0;
    step[0][0] = 0;     //ά��x���굱ǰλ��
    step[0][1] = 0;     //ά��y���굱ǰλ��
    int i=0,j;
    while(true){
        switch(command[i]){
            case 'U':step[0][1]++;
            break;
            case 'R':step[0][0]++;
            break;
        }
        if(count<obstaclesSize){
            for(j=0;j<obstaclesSize;j++){
                if(step[0][0] == obstacles[j][0] && step[0][1] == obstacles[j][1] && (step[0][0]<=obstacles[j][0] && step[0][1]<=obstacles[j][1])){
                        return false;
                }
            }
        }
        if(step[0][0] == x && step[0][1] == y) return true;
        i++;
        if(i == strlen(command)){
            i=0;
            count++;
        }
        if(step[0][0] >= x && step[0][1]>=y) return false;
    }

}
