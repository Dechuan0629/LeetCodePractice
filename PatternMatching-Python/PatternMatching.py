def main():
    a = Solution()
    p = 'bbbbbbbbbbbbbbabbbbb'
    v = 'ppppppppppppppjsftcleifftfthiehjiheyqkhjfkyfckbtwbelfcgihlrfkrwireflijkjyppppg'
    print(a.patternMatching(p,v))


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        temp_a = a = pattern.count('a')
        temp_b = b = pattern.count('b')
        judge = 0
        if(len(pattern)==1 and len(value)==0):return True
        if(len(pattern)!=0 and len(value)==0):return False
        if(len(pattern)==0):return not len(value)
        strlen = len(value)
        if(a==0):temp_a = strlen
        elif(b==0):temp_b = strlen
        for x in range(strlen//temp_a+1):  #x,y的长度不会超过总长度/个数
            for y in range(strlen//temp_b+1):
                if(a*x+b*y != strlen):      #应满足 ax+by = strlen
                    continue
                num = 0
                a_list = []
                b_list = []
                for i in range(len(pattern)):
                    if(pattern[i] == 'a'):
                        a_list.append(value[num:num+x])     #分割出相应长度的字符串放入列表，并判断a、b列表中元素是否全部相等
                        num+=x
                        if(len(set(a_list))!=1):break
                    if(pattern[i] == 'b'):
                        b_list.append(value[num:num+y])
                        num+=y
                        if(len(set(b_list))!=1):break
                    if(i==(len(pattern)-1)): judge = 1
                if(judge == 1):break
            if(judge == 1):break
        print(a_list,b_list)
        if(judge == 1):return True
        else:return False


if __name__ == '__main__':
    main()