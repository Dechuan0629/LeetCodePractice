class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) ==0
    def push(self,a):
        self.items.append(a)
    def pop(self):
        return self.items.pop()

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = Stack()
        s = s.split()         #去除所有空格，将所有单词保存进列表
        judge = 0
        for word in s:
            stack.push(word)     #依次将单词入栈，利用栈先进后出的特性，可以得到逆序后的字符串
        ans = ''
        while not stack.isEmpty():
            ans+=stack.pop()
            ans+=' '
        return ans.rstrip()       #去除尾部多出来的空格

def main():
    str1 = "       a! good   example       "
    test = Solution()
    print(test.reverseWords(str1))

if __name__ == '__main__':
    main()