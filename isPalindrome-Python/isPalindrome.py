import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(re.findall(r"\w",s)).lower()
        return temp == temp[::-1]

def main():
    test = Solution()
    s = "A man, a plan, a canal: Panama"
    print(test.isPalindrome(s))

if __name__ == '__main__':
    main()