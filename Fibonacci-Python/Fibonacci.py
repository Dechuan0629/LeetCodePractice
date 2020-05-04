class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        result = [0,1]
        for i in range(2,n+1):  #空间复杂度O（n），递归超时
            result.append(result[i-1]+result[i-2])
        return result[-1] % 1000000007

def main():
    test = Solution()
    print(test.fib(2))

if __name__ == '__main__':
    main()