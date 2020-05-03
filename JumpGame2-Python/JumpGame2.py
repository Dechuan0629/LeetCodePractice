class Solution:
    # 贪心，仅在跳跃位置更大时进行更新
    def jump(self, nums: list) -> int:
        steps = 0
        end = 0
        maxposition = 0
        for i in range(len(nums) - 1):
            maxposition = max(maxposition, nums[i] + i)
            if i == end:
                end = maxposition
                steps += 1
        return steps

    # 模拟跳的过程，递归，超时
    # def jump(self, nums: list) -> int:
    #     self.ans = []
    #     self.nums = nums
    #     for i in range(nums[0]):
    #         count = 0
    #         if i+1 >= len(nums):
    #             break
    #         self.go(nums[i+1],i+1,count+1)
    #     try:
    #         return min(self.ans)
    #     except ValueError:
    #         return 1
    #
    # def go(self,step,position,count):
    #     if step == 0 and position < len(self.nums)-1:
    #         return -1
    #     elif position >= len(self.nums)-1:
    #         self.ans.append(count)
    #         return 1
    #     for i in range(step):
    #         if position+i+1 >= len(self.nums):
    #             break
    #         self.go(self.nums[position+i+1],position+i+1,count+1)




def main():
    test = Solution()
    list1 = [0]
    print(test.jump(list1))


if __name__ == '__main__':
    main()