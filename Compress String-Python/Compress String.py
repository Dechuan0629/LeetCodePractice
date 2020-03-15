class Solution:
    def compressString(self, S: str) -> str:
        i = 0
        count_temp = 0
        str_result = ""
        for c in S:
            if i == 0 :
                count_temp+=1
                str_result+=c
                i+=1
                char_temp = c
                continue
            if c == char_temp:
                count_temp+=1
                i+=1
                char_temp = c
                if i == len(S):
                    str_result+=str(count_temp)
                continue
            else:
                str_result+=str(count_temp)
                count_temp = 1
                str_result+=c
                char_temp = c
                i+=1
                if i == len(S):
                    str_result+=str(count_temp)
        if(len(str_result)<len(S)):return str_result
        else:return S

def main():
    test = Solution()
    str1 = 'abbccd'
    str2 = test.compressString(str1)
    print(str2)

if __name__ == '__main__':
    main()