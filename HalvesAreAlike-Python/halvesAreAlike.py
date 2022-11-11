class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelDict = {'a':1,'e':1,'i':1,'o':1,'u':1}
        halfLen = len(s)//2
        strLeft = s[:halfLen]
        strRight = s[halfLen:]
        countL = 0
        countR = 0
        for i in range(halfLen):
            sL = strLeft[i].lower()
            sR = strRight[i].lower()
            countL += vowelDict.get(sL) if vowelDict.get(sL) != None else 0
            countR += vowelDict.get(sR) if vowelDict.get(sR) != None else 0
        return countL == countR
def main():
    test = Solution()
    print(test.halvesAreAlike("aiaiax"))

if __name__ == '__main__':
    main()