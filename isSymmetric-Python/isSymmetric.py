class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Build:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder.pop(0))
        i = inorder.index(node.val)   #先序遍历确定当前的根节点
        node.left = self.buildTree(preorder[:i], inorder[:i])     #中序遍历确定左右子树
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])  #递归创建即可
        return node

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def search(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            return search(left.left,right.right) and search(left.right,right.left)
        return search(root.left,root.right)

def main():
    build = Build()
    test = Solution()
    pre = [1,2,3,2,3]
    mid = [2,3,1,2,3]
    root = build.buildTree(pre,mid)
    print(test.isSymmetric(root))

if __name__ == '__main__':
    main()