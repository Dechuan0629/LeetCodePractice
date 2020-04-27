class Solution:
    def singleNumbers(self, nums: list) -> list:
        num = 0                #1.异或满足交换律，2.相同的数异或为0，3.任何数与0异或为本身
        for numi in nums:      #那么，如果是找一个单独出现的数，只需要将所有数异或得到的结果便是那个数
            num ^= numi        #本题有两数出现一次，将所有数异或的结果相当于将那两个单独出现的数做异或
        num = num&(~num+1)     #如1和6做异或，0001 ^ 0110 = 0111因为二进制每一位上不同的数异或为1，那么我们可以1和6做异或，从右往左第一个出现的1，就是两个数在二进制上第一个不相同的位出现的位置
        ans = [0,0]            #那么利用这个性质，我们可以利用这一位，将整个数组分为两组，一组在这个位上都为1，一组在这个位上都为0
        for numi in nums:      #那两个单独出现的数就一定分别出现在这两个组内，那么现在就相当于分别对每一组找出那一个出现一次的数，也就是两组分别进行一次所有数的异或运算，剩下的数就是结果
            if numi & num:ans[0]^=numi
            else:ans[1]^=numi
        return ans


def main():
    test = Solution()
    nums = [4,1,4,6]
    print(test.singleNumbers(nums))

if __name__ == '__main__':
    main()