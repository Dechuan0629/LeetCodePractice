class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            if length+i > len(haystack):
                return -1
            elif haystack[i:length+i] == needle:
                return i
        if len(haystack) == 0 and length == 0:
            return 0
        else:
            return -1

def main():
    haystack,needle = "","a"
    test = Solution()
    print(test.strStr(haystack,needle))

if __name__ == '__main__':
    main()
