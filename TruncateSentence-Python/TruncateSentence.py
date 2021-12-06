class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sList = s.split(" ")
        return " ".join(str(i) for i in sList[:k])


def main():
    test = Solution()
    s = "leetcode is a coding plateform !"
    print(test.truncateSentence(s,1))


if __name__ == '__main__':
    main()