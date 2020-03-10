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
    for(i=0;i<strlen(longUrl);i++){           //分离出网址和索取的文件地址，分别保存在str_site和str_file中
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
    for(p=str_file; *p; p++){                 //计算出文件地址的哈希值
        h+=*p;
    }
    itoa(h,hash,10);                          //文件hash值保存在hash字符串中

    char *tinyurl;                            //完成tinyurl_site和hash的拼接
    tinyurl = (char*)malloc(strlen(tinyurl_site)+strlen(hash));
    strcpy(tinyurl,tinyurl_site);
    strcat(tinyurl,hash);
    UrlDB(longUrl,hash,0);                    //将原始网址与对映的hash值送入Url数据库，0表示加密过程
    return tinyurl;
}

/** Decodes a shortened URL to its original URL. */
char* decode(char* shortUrl) {
    char *url1,*hash2;
    char *p;
    int count = 0;
    url1 = (char*)malloc(50);
    hash2 = (char*)malloc(10);
    for(p=shortUrl;*p;p++){           //取出tinyUrl中的hash值
        if(*p == '/'){
            count++;
        }
        if(count == 3){
            hash2 = p+1;
            break;
        }
    }
    url1 = UrlDB(shortUrl,hash2,1);   //将hash值送入Url数据库寻找原始Url，1表示解密过程
    return url1;
}

char* UrlDB(char *Url,char* hash1,int judge){  //当judge = 0时表示加密，当judge = 1时表示解密，简单完成哈希值与原始url的对映关系，后续可用数据库交互实现
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

