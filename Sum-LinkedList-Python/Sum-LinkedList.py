class Stack():
    def __init__(self):
        self.stack = []
    def IsEmpty(self)->bool:
        return len(self.stack)
    def pop(self):
        return self.stack.pop()
    def push(self,x) -> None:
        self.stack.append(x)

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1.next
        p2 = l2.next
        stack1 = Stack()
        stack2 = Stack()
        while p1!= None or p2!=None:    #利用两个栈实现两数从个位数按位相加
            if p1!=None:
                stack1.push(p1.val)
                p1 = p1.next
            if p2!=None:
                stack2.push(p2.val)
                p2 = p2.next
        carry = 0
        i = 0
        while stack1.IsEmpty() or stack2.IsEmpty():
            if stack1.IsEmpty() == False:
                temp1 = 0
            else:
                temp1 = stack1.pop()
            if stack2.IsEmpty() == False:
                temp2 = 0
            else:
                temp2 = stack2.pop()
            node = ListNode((temp1+temp2+carry)%10)
            if i == 0:
                temp = node
                i+=1
            else:
                node.next = temp           #头部插入
                temp = node
            carry = (temp1+temp2+carry)//10
        head = node
        if carry != 0:
            node = ListNode(carry)
            node.next = head
            head = node
        return head


def main():
    list1 = [9,7,3,6,5]
    list2 = [7,9,2,5]
    head1 = ListNode(None)
    head2 = ListNode(None)
    for idx,i in enumerate(list1):
        next = ListNode(i)
        if idx == 0:
            head1.next = next
        else:
            temp.next = next
        temp = next
    for idx,i in enumerate(list2):
        next = ListNode(i)
        if idx == 0:
            head2.next = next
        else:
            temp.next = next
        temp = next
    test = Solution()
    head = test.addTwoNumbers(head1,head2)
    while head!=None:
        print(head.val,end = "")
        head = head.next

if __name__ == '__main__':
    main()