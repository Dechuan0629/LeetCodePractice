#include <stdio.h>
#include <stdlib.h>

char* encode(char* longUrl);
char* UrlDB(char *Url,char* hash1,int judge);
char* decode(char* shortUrl);

int main()
{
    char *str_un;
    str_un = (char*)malloc(50);
    char *str_en,*str_decry;
    scanf("%s",str_un);
    printf("\nOriginal Url:%s\n\n",str_un);
    str_en = encode(str_un);
    free(str_un);
    printf("Encreypted Url:%s\n\n",str_en);
    str_decry = decode(str_en);
    free(str_en);
    printf("Decreypter Url:%s\n",str_decry);
    free(str_decry);
    return 0;

}

char* encode(char* longUrl) {
    int h = 0,i,count = 0,j = 0;
    char *str_site,*str_file,*hash,*tinyurl_site;
    str_site = (char*)malloc(20);
    str_file = (char*)malloc(50);
    hash = (char*)malloc(10);
    tinyurl_site = (char*)malloc(20);
    tinyurl_site = "http://tinyurl.com/";
    for(i=0;i<strlen(longUrl);i++){           //�������ַ����ȡ���ļ���ַ���ֱ𱣴���str_site��str_file��
        if(count<3){
            str_site[i] = longUrl[i];
            if(longUrl[i] == '/') count++;
            if(count == 3) str_site[i+1] = '\0';
        }
        else{
            str_file[j] = longUrl[i];
            j++;
        }
    }
    str_file[j] = '\0';
    char *p;
    for(p=str_file; *p; p++){                 //������ļ���ַ�Ĺ�ϣֵ
        h+=*p;
    }
    itoa(h,hash,10);                          //�ļ�hashֵ������hash�ַ�����

    char *tinyurl;                            //���tinyurl_site��hash��ƴ��
    tinyurl = (char*)malloc(strlen(tinyurl_site)+strlen(hash));
    strcpy(tinyurl,tinyurl_site);
    strcat(tinyurl,hash);
    UrlDB(longUrl,hash,0);                    //��ԭʼ��ַ���ӳ��hashֵ����Url���ݿ⣬0��ʾ���ܹ���
    return tinyurl;
}

/** Decodes a shortened URL to its original URL. */
char* decode(char* shortUrl) {
    char *url1,*hash2;
    char *p;
    int count = 0;
    url1 = (char*)malloc(50);
    hash2 = (char*)malloc(10);
    for(p=shortUrl;*p;p++){           //ȡ��tinyUrl�е�hashֵ
        if(*p == '/'){
            count++;
        }
        if(count == 3){
            hash2 = p+1;
            break;
        }
    }
    url1 = UrlDB(shortUrl,hash2,1);   //��hashֵ����Url���ݿ�Ѱ��ԭʼUrl��1��ʾ���ܹ���
    return url1;
}

char* UrlDB(char *Url,char* hash1,int judge){  //��judge = 0ʱ��ʾ���ܣ���judge = 1ʱ��ʾ���ܣ�����ɹ�ϣֵ��ԭʼurl�Ķ�ӳ��ϵ�������������ݿ⽻��ʵ��
    static char *hash_temp,*Url_temp;
    if(judge == 0){
        hash_temp = (char*)malloc(strlen(hash1));
        Url_temp = (char*)malloc(strlen(Url));
        strcpy(hash_temp,hash1);
        strcpy(Url_temp,Url);
        return 1;
    }

    else if(judge == 1){
        if(strcmp(hash1,hash_temp)==0){
            return Url_temp;
        }
        else return 0;
    }
}

