class Solution:
    def longestPalindrome(self, s: str) -> str:
        #滑动窗口暴力法
        for i in range(len(s)-1):
            for j in range(len(s)-(len(s)-1-i)):
                temp = s[j:j+len(s)-1-i]
                if temp == temp[::-1]:
                    return temp
        return ""

def main():
    test = Solution()
    s = "babad"
    print(test.longestPalindrome(s))

if __name__ == '__main__':
    main()