#include <stdio.h>
#include <stdlib.h>

char* gcdOfStrings(char * str1, char * str2);
char* split(char *str,int len);

int main()
{
    char str[10] = "aaaaaaaa";
    char str2[10] = "aa";
    char *str3;
    //str3 = gcdOfStrings(str,str2);
    printf("%s",gcdOfStrings(str,str2));
    free(str3);
    return 0;
}

char* gcdOfStrings(char * str1, char * str2){
    int i,j,len1,len2,len3;
    int judge = 0;
    char *str;
    if(strlen(str1)>strlen(str2)){  //len1---small one
         len1 = strlen(str2);
         len2 = strlen(str1);
    }
    else{
         len1 = strlen(str1);
         len2 = strlen(str2);
    }
    str = (char*)calloc(len1,sizeof(char));
    if(len2%len1!=0) return str;
    for(i=0;i<len1;i++){
        if(len2%(i+1)!=0 || len1%(i+1)!=0) continue;   //当偶数段长度截取奇数段长度时，无意义，同理奇数段，直接跳过。
        for(j=0;j<len2/(i+1);j++){
            if(strcmp(split(str1+j*(len2/(len2/(i+1))),i+1),split(str2,i+1))){      //j*(len2/(len2/(i+1))) 得到每次截取的步长的首地址
                break;
            }
            if(j==len2/(i+1)-1 && ((i+1)!=1 || len1==1)){
                judge = 1;
                strcpy(str,split(str2,i+1));
            }
        }
        if(judge==1) break;
    }
    return str;
}

char* split(char *str,int len){                    //字符串截取函数
    char *str1;
    int i;
    str1 = (char*)calloc(len,sizeof(char));
    for(i=0;i<len;i++) *(str1+i)=*(str+i);
    return str1;
}
