class Solution:
    def search(self, nums: list, target: int) -> int:
        if target not in nums:
            return -1
        count = 0
        judge = 0
        self.nums = nums
        for i in range(len(nums)-1):           #找到翻转点
            if nums[i] > nums[i+1]:
                count = i
                judge = 1
                break
        if count == 0 and judge!=1:
            count = len(nums)-1
        if target >= nums[0]:                  #判断数在翻转点的哪一半，接着执行二分查找
            ans = self.half(0,count,target)
        else:
            ans = self.half(count+1,len(nums)-1,target)
        return ans

    def half(self,left,right,target):
        mid = int(left + (right - left)/2)
        if self.nums[mid] == target:
            return mid
        elif self.nums[mid] > target:
            return self.half(left,mid-1,target)
        else:
            return self.half(mid+1,right,target)


def main():
    test = Solution()
    nums = [1,2]
    print(test.search(nums,2))

if __name__ == '__main__':
    main()