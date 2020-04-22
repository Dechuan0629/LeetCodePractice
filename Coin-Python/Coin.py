class Solution:
    def waysToChange(self, n: int) -> int:  #类似完全背包问题
        coin = [25,10,5,1]
        value = [i-i for i in range(n+1)]
        value[0] = 1
        for c in coin:
            for i in range(c,n+1):
                value[i] += value[i-c]
        return int(value[n] % (10e8+7))


def main():
    test = Solution()
    print(test.waysToChange(1000000))

if __name__ == '__main__':
    main()