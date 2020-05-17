class Solution:
    def maxProduct(self, nums:list) -> int:
        # positive = [1]  #当数组中不存在0时，可以用 M[I,J] = M[0,J] / M[0,I]得到最大组
        # negetive = []
        # res = 1
        # for num in nums:
        #     res *= num
        #     if res >= 0:
        #         positive.append(res)
        #     else:
        #         negetive.append(res)
        # if len(negetive) <= 1:
        #     return positive[-1]//positive[0]
        # return max(positive[-1]//positive[0],negetive[-1]//negetive[0])
        temp = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            temp[i] *= temp[i - 1] or 1
        return max(max(nums), max(temp))

def main():
    test = Solution()
    nums = [0,7,9,-2,-5,-1,12]
    print(test.maxProduct(nums))

if __name__ == '__main__':
    main()