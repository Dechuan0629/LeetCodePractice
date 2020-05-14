class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        ans,sum = 0,0
        map = {0:1}
        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in map:
                ans += map[sum-k]
            if sum not in map:
                map[sum] = 0
            map[sum] +=1
        return ans

def main():
    test = Solution()
    nums = [1,1,1,2]
    print(test.subarraySum(nums,2))

if __name__ == '__main__':
    main()