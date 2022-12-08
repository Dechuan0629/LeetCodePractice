class Solution:
    ans = []
    def letterCombinations(self, digits: str) -> list:
        # 清空一下，leetcode真坑
        self.ans = []
        if len(digits) == 0: return []
        numDict = {'2':['a','b','c'],'3':['d','e','f'],
                   '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
                   '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        letters = []
        for ch in digits:
            letters.append(numDict[ch])
        self.combin(letters,0,'')
        return self.ans

    def combin(self,wordVec,index,chr):
        for letter in wordVec[index]:
            tempLetter = chr + letter
            if index == len(wordVec) - 1:
                self.ans.append(tempLetter)
            else:
                self.combin(wordVec,index+1,tempLetter)

#简单递归回溯算法
def main():
    test = Solution()
    s = "3"
    print(test.letterCombinations(s))

if __name__ == '__main__':
    main()