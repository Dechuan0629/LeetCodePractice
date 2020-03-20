class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:  #根据题意，需要满足的条件可化为方程 ax+by = z
        if x+y<z:return False
        if x==0 and y==0 : return not bool(z)
        elif x==0:return bool(y==z or z==0)
        elif y==0:return bool(x==z or z==0)
        if z % self.gcd(x,y) == 0:return True                   #根据裴蜀定理，有x,y的最大公约数n，满足任意整数a，b，ax+by 都一定是n的倍数
        else:return False                                       #因此，根据定理，ax+by = z有解，当且仅当z为最大公约数n的倍数
                                                                #所以满足True的条件为，z对x，y的最大公约数n求余数的结果为0
    def gcd(self,a, b):
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

def main():
    test = Solution()
    print(test.canMeasureWater(0,2,0))


if __name__ == '__main__':
    main()