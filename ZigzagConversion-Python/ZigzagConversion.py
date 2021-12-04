class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        tempMatrix = [[] for i in range(numRows)]
        lineCount = 0
        for ch in s:  #按照 0,1...,numRows-1,..1,0,1....numRows-1的顺序，插入到对应行中，然后拼接即可
            if lineCount == 0:
                addFlag = True
            elif lineCount == numRows - 1:
                addFlag = False
            tempMatrix[lineCount]+=ch
            if addFlag:
                lineCount += 1
            else:
                lineCount -= 1
        return "".join([ch for tempList in tempMatrix for ch in tempList])

def main():
    test = Solution()
    print(test.convert("PAYPALISHIRING",3))

if __name__ == '__main__':
    main()