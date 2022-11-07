class Solution:
    def removeDuplicates(self, nums: list) -> int:
        count = 0
        temp = -99999
        for num in nums:
            if temp != num:
                count+=1
                temp = num
        return count

def main():
    test = Solution()
    nums = [1,1,2,3,3,3,6,7,8,9,9,9,9,10]
    print(test.removeDuplicates(nums))

if __name__ == '__main__':
    main()