class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numS,ans = list(map(lambda x:int(x),"".join(list(map(lambda ch:str(ord(ch)-96),s))))),0
        for i in range(k):
            ans = sum(numS)
            numS = list(map(lambda x:int(x),list(str(ans))))
        return ans


def main():
    test = Solution()
    s = "zaciew"
    print(test.getLucky(s,100))

if __name__ == '__main__':
    main()