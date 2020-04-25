import bisect
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        ans = []
        temp = []
        for listnode in lists:
            while listnode!=None:
                idx = bisect.bisect_right(temp,listnode.val)  #利用bisect库得到插入排序时的下标位置
                ans.insert(idx,listnode)                      #将node放入到相应位置的列表中，得到有序的节点列表
                temp[idx:idx] = [listnode.val]
                listnode = listnode.next
        for i in range(len(ans)):                             #将有序的节点列表连接起来即可
            if i == len(ans)-1:
                break
            else:
                ans[i].next = ans[i+1]
        try:
            return ans[0]
        except IndexError:
            return None

def main():
    test = Solution()
    list1 = [[1,2,3,91],[2,6,9],[7,9,11],[0,1]]
    root = []
    for temp in list1:
        for i,num in enumerate(temp):
            node = ListNode(num)
            if i == 0:
                temp_root = node
            else:
               pre.next = node
            pre = node
        root.append(temp_root)
    ans = test.mergeKLists(root)
    while ans!=None:
        print(ans.val)
        ans = ans.next

if __name__ == '__main__':
    main()