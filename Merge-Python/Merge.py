class Stack():
    def __init__(self):
        self.stack = []
    def push(self,x) ->None:
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def empty(self) ->bool:
        return not len(self.stack)
    def __len__(self) ->int:
        return len(self.stack)

class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort()   #按行首元素进行排序
        stack = Stack()
        for i in range(len(intervals)-1,-1,-1): #从后往前入栈
            stack.push(intervals[i])
        ans = []
        while not stack.empty():
            if stack.__len__() == 1:       #一次pop两个，能连接就push回连接后的结果，不能连接就将前一个append到列表中，后一个push回栈
                ans.append(stack.pop())
                break
            temp1 = stack.pop()
            temp2 = stack.pop()
            if temp1[1] >= temp2[0] :
                if temp1[1] >= temp2[1]:
                    res  = [temp1[0],temp1[1]]
                else:
                    res = [temp1[0],temp2[1]]
                stack.push(res)
            else:
                ans.append(temp1)
                stack.push(temp2)
        return ans

def main():
    test = Solution()
    list1 = [[1,4],[2,3]]
    print(test.merge(list1))

if __name__ == '__main__':
    main()