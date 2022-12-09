class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        sumNum = 0
        count = 0
        while sumNum <= n:
            sumNum += 3**count
            count += 1
        for i in range(2**count):
            binNums = bin(i)[2:].zfill(count)
            sum = 0
            for index,binNum in enumerate(binNums[::-1]):
                sum += int(binNum)*(3**index)
                if sum == n:
                    return True
        return False

#因为题目n最大10000000
#因此3**0 + 3**1 + 3**2 + ... + 3**n
#n其实最大就15
#则其实本题暴力解法，最多就2**15=32768种结果，二进制枚举能过，时间复杂度2**n
#更简单的做法，可以将数转化位为3进制
def main():
    test = Solution()
    print(test.checkPowersOfThree(99))

if __name__ == '__main__':
    main()