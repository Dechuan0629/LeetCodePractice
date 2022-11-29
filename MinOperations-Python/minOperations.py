class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 0: return 0
        c1 = int(s[0])
        c2 = (c1+1)%2
        ansC1,ansC2 = 0,0
        # 利用交替字符进行位校验，取次数最小的
        for ch in s:
            c1 = c1 % 2
            c2 = c2 % 2
            if str(c1) != ch:
                ansC1 += 1
            if str(c2) != ch:
                ansC2 += 1
            c1+=1
            c2+=1
        return min(ansC1,ansC2)

def main():
    test = Solution()
    s = "10010100"
    print(test.minOperations(s))

if __name__ == '__main__':
    main()