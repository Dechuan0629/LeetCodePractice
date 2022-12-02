import random
class Solution:
    def minOperations(self, boxes: str) -> list:
        indexList = [index for index,ch in enumerate(boxes) if ch == '1']
        ans = []
        for i in range(len(boxes)):
            tempSum = 0
            for j in indexList:
                tempSum += abs(j-i)
            ans.append(tempSum)
        return ans


def main():
    test = Solution()
    s = ""
    for i in range(2000):
        s += str(random.randint(0,1))
    print(test.minOperations(s))

if __name__ == '__main__':
    main()