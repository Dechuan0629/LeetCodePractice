class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.search(root, -999999)
        return self.count

    def search(self, node: TreeNode, max: int):
        if node == None or node.val == None:
            return
        if node.val >= max:
            max = node.val
            self.count += 1
        self.search(node.left, max)
        self.search(node.right, max)

def main():
    test = Solution()
    treeList = [3,1,4,2,None,5,7]
    # treeList[i].left = treeList[i*2+1]
    # treeList[i].right = treeList[i*2+2]
    tree = [TreeNode(node) for node in treeList]
    for index,node in enumerate(tree):
        if index*2+1 >= len(tree):break
        node.left = tree[index*2+1]
        node.right = tree[index*2+2]
    print(test.goodNodes(tree[0]))

if __name__ == '__main__':
    main()