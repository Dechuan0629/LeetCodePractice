class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)): #暴力解法，判断每一个字符的最长无重复字符子串
            j = i
            temp = []
            if len(s)-1-i < ans:
                break
            while j < len(s):
                if s[j] not in temp:
                    temp.append(s[j])
                    ans = max(ans,len(temp))
                    j+=1
                else:
                    break
        return ans

def main():
    test = Solution()
    str1 = "abcaq"
    print(test.lengthOfLongestSubstring(str1))

if __name__ == '__main__':
    main()