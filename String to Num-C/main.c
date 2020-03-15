#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
    int i,j;
    double temp = 0;
    for(i=0;i<150000;i++){
        for(j=0;j<75000;j++){
            if(temp>=0) temp+=0.1;
        }
    }
    printf("%lf",temp);
    return 0;
}

bool isNumber(char* s){

}
