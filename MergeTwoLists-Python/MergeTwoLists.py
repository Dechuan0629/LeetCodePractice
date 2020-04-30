class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(None)
        if l1 == None and l2 == None:
            return temp
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        while l1 != None and l2 != None: #利用两个指针指向两个有序链表，每次连接较小的一个
            if l1.val <= l2.val:         #同时指针向后移一位，直到某个指针指向None，接着将另一个不为0的指针所有元素连接上即为结果
                if temp.val == None:     #时间复杂度O(n)，空间度复杂为O(1),只申请了常量空间的表头
                    root = temp
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                if temp.val == None:
                    root = temp
                temp.next = l2
                temp = l2
                l2 = l2.next
        if l1 == None:
            temp.next = l2
        else:
            temp.next = l1
        return root.next

def main():
    test = Solution()
    nums = [[100,111],[9,11,15,1024]]
    root = []
    for line in nums:
        if len(line) == 0:
            root.append(None)
            continue
        for i,num in enumerate(line):
            node = ListNode(num)
            if i == 0:
                temp_root = node
            else:
                temp.next = node
            temp = node
        root.append(temp_root)
    root = test.mergeTwoLists(root[0],root[1])
    while root != None:
        print(root.val)
        root = root.next

if __name__ == '__main__':
    main()