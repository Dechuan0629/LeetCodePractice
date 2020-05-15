class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class mystack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def empty(self)->bool:
        return len(self.stack)

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = mystack()
        pre = ListNode(None)
        judge = False
        ans = None
        while head:   #一次ac，利用额外的栈空间来存放节点
            for i in range(k):
                stack.push(head)
                if head.next == None and i!=(k-1):   #这个情况为真，说明已经到最后一个且并没有整数分割
                    pre.next = stack.stack[0]
                    judge = True
                    break
                head = head.next
            if judge:
                break
            n = 0
            temp_head = None
            while stack.empty():   #将栈中的节点逆序连接
                node = stack.pop()
                if n == 0:
                    if ans == None:
                        ans = node
                    temp_head = node
                    n+=1
                else:
                    pre_node.next = node
                pre_node = node
            if head == None:
                node.next = None
            pre.next = temp_head   #将上一个分组的最后一个节点连接到本分组
            pre = node
        return ans

def main():
    test = Solution()
    for i,x in enumerate([1,2,3,4,5,6,7]):
        node = ListNode(x)
        if i == 0:
            root = node
        else:
            pre_node.next = node
        pre_node = node
    ans = test.reverseKGroup(root,3)
    while ans:
        print(ans.val,end="")
        ans = ans.next

if __name__ == '__main__':
    main()