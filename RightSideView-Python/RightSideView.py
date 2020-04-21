class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def breadth_travel(self,root):  # 广度
        if root is None:
            return 0
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self,root):  # 深度-先序
        if root:
            print(root.val, end=" ")
            self.search(root.left)
            self.search(root.right)


class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        layer = []
        ans = [root.val]
        layer.append(root)
        while True:          #按层访问，将每一层的节点放入列表，访问列表的最后一个值，也就是每一层的最后一个值便是结果
            temp = []
            for i in layer:
                if i.left!=None:
                    temp.append(i.left)
                if i.right!=None:
                    temp.append(i.right)
            layer = temp
            if len(layer) == 0:
                break
            ans.append(layer[-1].val)
        return ans

def main():
    root,b,c,d,e,f,g,h,i = [TreeNode(i) for i in [1,2,3,5,4,9,11,2,7]]
    root.left,root.right= b,c
    b.right,c.right = d,e
    d.left,d.right,e.right = f,g,h
    f.left = i
    test = Solution()
    print(test.rightSideView(root))


if __name__ == '__main__':
    main()