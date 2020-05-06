class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = t
        self.ori = []
        self.pruned = []
        self.search(s,self.ori)
        self.prune(s,TreeNode(None),'root')
        self.search(s,self.pruned)
        return self.ori == self.pruned      #判断剪枝前后两棵树是否相等，相等则证明t为s的子树
    def prune(self,root,pre,side):          #当出现s的节点与t的根节点相同时，将s剪枝，然后将t全部嫁接上去
        if root:
            if root.val == self.t.val:
                if side == 'left':
                    pre.left = self.t
                elif side == 'right':
                    pre.right = self.t
                else:
                    pre = self.t
            else:
                self.prune(root.left,root,'left')
                self.prune(root.right,root,'right')
    def search(self,root,temp):
        if root:
            temp.append(root.val)
            self.search(root.left,temp)
            self.search(root.right,temp)

def main():
    test = Solution()
    root1,a,b,c,d = [TreeNode(x) for x in [3,4,5,1,2]]
    root1.left,root1.right = a,b
    a.left,a.right = c,d
    root2,e,f = [TreeNode(x) for x in [4,1,2]]
    root2.left,root2.right = e,f
    print(test.isSubtree(root1,root2))


if __name__ == '__main__':
    main()