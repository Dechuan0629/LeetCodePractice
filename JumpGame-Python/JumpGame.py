class Solution:
    def canJump(self, nums: list) -> bool:
    #   贪心算法，到当前位置接着跳的最大距离如果能够大于等于最后一个位置，便说明能够到达
        count = 0
        for i in range(len(nums)):
            if i > count:   #   count保存着当前位置，i 大于count了说明已经到最后一个位置了但此时最多能到达的位置无法达到
                return False
            count = max(count,i+nums[i])
        return True

    #   暴力求解，会超时
    #     self.nums = nums
    #     if self.Check(0,0) == len(nums)-1:
    #         return True
    #     else:
    #         return False
    #
    # def Check(self,i,ans):
    #     if i >= len(self.nums) or i == len(self.nums)-1 or self.nums[i] == 0:
    #         return ans
    #     for j in range(1,self.nums[i]+1):
    #         ans += j
    #         ans = self.Check(i+j,ans)
    #         if ans == len(self.nums)-1:
    #             break
    #         else:
    #             ans -= j
    #     return ans

def main():
    test = Solution()
    list1 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3]
    print(test.canJump(list1))

if __name__ == '__main__':
    main()