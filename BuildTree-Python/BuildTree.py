class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder.pop(0))
        i = inorder.index(node.val)   #先序遍历确定当前的根节点
        node.left = self.buildTree(preorder[:i], inorder[:i])     #中序遍历确定左右子树
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])  #递归创建即可
        return node

def main():
    test = Solution()
    pre = [3,9,21,20,15,7]
    mid = [21,9,3,15,20,7]
    root = test.buildTree(pre,mid)
    tree_queue = [root]
    check = 0
    while tree_queue:
        node = tree_queue.pop(0)
        print(node.val,end=" ")
        if node.left:
            tree_queue.append(node.left)
        if node.right:
            tree_queue.append(node.right)

if __name__ == '__main__':
    main()