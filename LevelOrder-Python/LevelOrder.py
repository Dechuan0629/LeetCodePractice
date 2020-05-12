class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if root == None:
            return []
        queue_current,queue_next = [],[root]
        ans = []
        while len(queue_next) != 0:     #分为两个队列访问，一个队列保存当前需要访问的层，一个队列保存下一层但不立即访问
            temp = []
            queue_current += queue_next
            queue_next = []
            for node in queue_current:
                temp.append(node.val)
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)
            queue_current = []
            ans.append(temp)
        return ans

def main():
    test = Solution()
    root,b,c,d,e = [TreeNode(x) for x in [3,9,20,15,7]]
    root.left,root.right = b,c
    c.left,c.right = d,e
    print(test.levelOrder(root))


if __name__ == '__main__':
    main()
