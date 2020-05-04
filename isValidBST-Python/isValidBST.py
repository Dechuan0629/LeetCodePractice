class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.check = []
        self.judge = True
        self.search(root)
        return self.judge

    def search(self,root):             #中序遍历搜索树，当得到的上升序列出现无序时，为无效二叉搜索树
        if root and self.judge:
            self.search(root.left)
            if len(self.check) != 0 and root.val <= self.check[-1]:
                self.judge = False
            self.check.append(root.val)
            self.search(root.right)

def main():
    test = Solution()
    nums = [1,4,6,5,7]
    # nums = [1,2,3]
    root,b,c,d,e = [TreeNode(x) for x in nums]
    root.left , root.right = b,c
    c.left , c.right = d,e
    print(test.isValidBST(root))

if __name__ == '__main__':
    main()