class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp_root = root
        self.temp = []
        self.search(temp_root)       #进行一次中序遍历
        p_idx = self.temp.index(p.val)
        q_idx = self.temp.index(q.val)
        while True:
            mid_idx = self.temp.index(temp_root.val)   #接着执行二分查找
            if (p_idx <= mid_idx and q_idx >= mid_idx) or (q_idx <= mid_idx and p_idx >= mid_idx):   #当所找两数处于根节点两侧时，即为结果
                return temp_root
            elif p_idx < mid_idx and q_idx < mid_idx:
                temp_root = temp_root.left
            else:
                temp_root = temp_root.right

    def search(self,root):
        if root:
            self.search(root.left)
            self.temp.append(root.val)
            self.search(root.right)

def main():
    test = Solution()
    root,b,c,d,e,f,g,h,i = [TreeNode(x) for x in [3, 5, 1, 6, 2, 0, 8, 7, 4]]
    root.left,root.right = b,c
    b.left,b.right,c.left,c.right = d,e,f,g
    e.left,e.right = h,i
    p = TreeNode(5)
    q = TreeNode(1)
    print(test.lowestCommonAncestor(root,p,q).val)

if __name__ == '__main__':
    main()