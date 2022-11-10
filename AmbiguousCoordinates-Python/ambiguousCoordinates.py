import re

class Solution:
    def ambiguousCoordinates(self, s: str) -> list:
        s = s[1:-1]
        part = []
        for i in range(len(s)):
            if i == len(s) - 1:break
            part.append([s[:i+1],s[i+1:]])
        ans = []
        for pair in part:
            left = []
            right = []
            for i in range(len(pair[0])):
                if i == len(pair[0]) - 1:
                    left.append(pair[0])
                else:
                    temp = list(pair[0])
                    temp.insert(i+1,".")
                    left.append("".join(temp))
            for j in range(len(pair[1])):
                if j == len(pair[1]) - 1:
                    right.append(pair[1])
                else:
                    temp = list(pair[1])
                    temp.insert(j+1,".")
                    right.append("".join(temp))
            for leftStr in left:
                for rightStr in right:
                    if self.isLegalNum(leftStr) and self.isLegalNum(rightStr):
                        ans.append("("+leftStr+", "+rightStr+")")
        return ans

    def isLegalNum(self,s:str) -> bool:
        patternL = "^([1-9]{1}[0-9]*)|0$"
        patternR = "^[0-9]*[1-9]$"
        strs = s.split(".")
        if len(strs) == 1: return re.match(patternL,s) != None
        return re.match(patternL,strs[0]) != None and re.match(patternR,strs[1]) != None

def main():
    test = Solution()
    print(test.ambiguousCoordinates("(1234809700001300010130497134085729830012983091)"))

#需要从一个字符串内，找出两两一组的合法数字
#1.先列出所有能两两组合的情况，字符串数字长度为x，则组合数最多为x-1种
#2.找出每个两两一组的组合内，能形成合法数字的情况
#3.小数情况，其实和上述两两组合的情况一致

if __name__ == '__main__':
    main()