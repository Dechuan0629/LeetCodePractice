class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1,p2 = head,head
        for i in range(k-1):             #快慢指针，快指针走到慢指针k个之前，当快指针走到最后时，慢指针指向的就是结果
            p2 = p2.next
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
        return p1

def main():
    test = Solution()
    nums = [1,2,3,4,5]
    for i,num in enumerate(nums):
        node = ListNode(num)
        if i == 0:
            head = node
        else:
            temp_root.next = node
        temp_root = node
    ans = test.getKthFromEnd(head,2)
    while ans:
        print(ans.val,end="->")
        ans = ans.next
    print(None)

if __name__ == '__main__':
    main()