import numpy as np
class Solution:
    def massage(self, nums: list) -> int:
        temp1,temp2,ans = 0,0,0   #temp1保留着前一个值的最大值，temp2保留着前面第二个值的时候的最大值，ans得到当前最大值，由max决定是否更新
        for i in range(len(nums)):
            ans = max(temp1,temp2+nums[i])
            temp2 = temp1
            temp1 = ans
        return ans


def main():
    list1 = [2,1,4,5,3,1,1,3]
    test = Solution()
    print(test.massage(list1))



if __name__ == '__main__':
    main()