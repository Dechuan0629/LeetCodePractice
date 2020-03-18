#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str[1000] = "aaaaaaaAAAz";
    int result = longestPalindrome(str);
    printf("%d",result);
    return 0;
}

int longestPalindrome(char * s){
    int table[52] = {0};
    int count = 0;
    int i,judge = 0;
    for(i=0;i<strlen(s);i++){     //构建字母个数表
        if(s[i]>=97 && s[i]<=122){
            table[s[i]-97]++;
        }
        else if(s[i]>=65 && s[i]<=90){
            table[s[i]-39]++;
        }
    }

	for(i=0;i<52;i++){
		if(table[i]%2==0){       //偶数个的直接相加
			count+=table[i];
		}
		else{
			judge = 1;           //judge判断是否存在奇数个的字母，如果有，结果应返回+1
			count+=(table[i]-1);   //奇数个的减一后相加
		}
	}
	if(judge == 1) return count+1;
	return count;
}
