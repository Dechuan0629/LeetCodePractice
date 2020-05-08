class Solution:
    def mySqrt(self, x: int) -> int:
        k = len(str(x))/2
        a,b = (2.5*(10**(k-1)))**2,(5*(10**(k-1)))**2   #一种牛顿迭代取初始点的方法，可以保证在5次内迭代到结果
        if x < a:
            xn = 5*(10**(k-2)) + x/10**k/2
        elif x > b:
            xn = 10**(k-1) + x/10**k/2
        else:
            xn = 2.5*(10**(k-1)) + x/10**k/2

        while True:
            xn = xn-((xn**2-x)/(2*xn))  #牛顿迭代法，X（n+1） = X（n） - f（X（n））/f`（X（n））
            if abs(xn**2 - x) <= 10e-7:
                break
        return xn

def main():
    test = Solution()
    print(test.mySqrt(165481221241))

if __name__ == '__main__':
    main()