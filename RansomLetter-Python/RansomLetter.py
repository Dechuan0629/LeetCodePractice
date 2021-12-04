class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: #简单计数问题，保证magazine中相应字符的数量大于等于ransomNote即可
        ransomMap = [0 for i in range(26)]
        for ch in magazine: #生成杂志字符表
            ransomMap[ord(ch)-ord('a')]+=1
        for ch in ransomNote:
            ransomMap[ord(ch)-ord('a')]-=1
            if(ransomMap[ord(ch)-ord('a')]) < 0:
                return False
        return True




def main():
    test = Solution()
    print(test.canConstruct("aaabc","qqckalkqaaabc"))


if __name__ == '__main__':
    main()