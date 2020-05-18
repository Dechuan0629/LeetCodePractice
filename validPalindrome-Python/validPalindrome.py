class Solution:
    def validPalindrome(self, s: str) -> bool:
        if ''.join(reversed(s)) == s:
            return True
        i , j = 0, len(s)-1
        temp = list(s)
        while i < j:
            if temp[i] == temp[j]:  #两个指针从两边开始判别，当找到一个不同时，去掉这个如果是回文就返回True，否则返回False
                i+=1
                j-=1
                continue
            if temp[0:i]+temp[i+1:] == list(reversed(temp[0:i]+temp[i+1:])) or temp[0:j]+temp[j+1:] == list(reversed(temp[0:j]+temp[j+1:])):
                return True
            else:return False

def main():
    test = Solution()
    s = "abbam"
    print(test.validPalindrome(s))

if __name__ == '__main__':
    main()