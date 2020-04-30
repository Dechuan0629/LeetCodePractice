class Solution:
    def isHappy(self, n: int) -> bool:
        temp = []
        temp1 = []
        while True:
            num = 0
            for i in str(n):
                num+=(int(i)**2)
            if num == 1:
                return True
            n = num
            temp.append(num)
            if set(temp) == set(temp1):  #当前一个数组和当前数组相同时，说明出现了循环数了
                return False
            temp1 = temp.copy()


def main():
    test = Solution()
    print(test.isHappy(19))


if __name__ == '__main__':
    main()