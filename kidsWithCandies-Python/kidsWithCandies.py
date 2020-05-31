class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        max_num = max(candies)
        return [candy+extraCandies>=max_num for candy in candies]

def main():
    test = Solution()
    can = [2,3,5,1,3]
    print(test.kidsWithCandies(can,3))

if __name__ == '__main__':
    main()