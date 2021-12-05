class Solution:
    def superPow(self, a, b) -> int:   #   a * b mod x  ==   ((a mod x) * (b mod x)) mod x
        ans = 1
        bLength = len(b)
        count = len(b)
        for num in reversed(b):
            temp = 1
            for i in range(num):
                temp *= a**(10**(bLength-count))%1337
            temp = temp % 1337
            ans *= temp
            ans = ans % 1337
            count-=1
        return ans

def main():
    test = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    print(test.superPow(2,nums))


if __name__ == '__main__':
    main()