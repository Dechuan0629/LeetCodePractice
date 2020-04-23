import bisect
class Solution:
    def reversePairs(self, nums: list) -> int:
        temp = []
        ans = 0
        for i,num in enumerate(nums):    #与后面的数相比较，类似于排序的过程，利用bisect模块可以得到插入排序时的位置
            idx = bisect.bisect_right(temp,num)
            ans += (i-idx)                 #利用它在nums中的位置减去插入排序到新数组中的位置即可以得到在前面的数中比它大的数有多少
            temp[idx:idx] = [num]
        print(temp)
        return ans

def main():
    test = Solution()
    list1 = [7,5,6,4,11,3,2,17,0,9]
    print(test.reversePairs(list1))


if __name__ == '__main__':
    main()