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
    for(i=0;i<strlen(s);i++){     //������ĸ������
        if(s[i]>=97 && s[i]<=122){
            table[s[i]-97]++;
        }
        else if(s[i]>=65 && s[i]<=90){
            table[s[i]-39]++;
        }
    }

	for(i=0;i<52;i++){
		if(table[i]%2==0){       //ż������ֱ�����
			count+=table[i];
		}
		else{
			judge = 1;           //judge�ж��Ƿ��������������ĸ������У����Ӧ����+1
			count+=(table[i]-1);   //�������ļ�һ�����
		}
	}
	if(judge == 1) return count+1;
	return count;
}
