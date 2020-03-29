class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        list1 = [x for x in range(n)]       #列表生成式
        i = 0
        while len(list1)!=1:
            i = (i-1+m)% n                  #当前的位置应该是前一个位置加上需要位移的m长度，对n求模得到回环的模型
            del(list1[i])                   #i-1是因为从列表中删去一个数字后，后面的数字会向前移一位
            n -=1                           #n-1得到新的列表的总长度
        return list1[0]

def main():
    test = Solution()
    print(test.lastRemaining(10000,9))

if __name__ == '__main__':
    main()