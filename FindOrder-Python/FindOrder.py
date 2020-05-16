class gragh:
    def __init__(self,x):
        self.val = x
        self.next = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        my_gragh = {}
        ans = []
        for point in prerequisites:  #创建图
            if point[0] not in my_gragh:
                my_gragh[point[0]] = {'node':gragh(point[0]),'no_pre':False}
                current = my_gragh[point[0]]['node']
            else:
                my_gragh[point[0]]['no_pre'] = False
                current = my_gragh[point[0]]['node']
            if point[1] not in my_gragh:
                my_gragh[point[1]] = {'node':gragh(point[1]),'no_pre':True}
                pre = my_gragh[point[1]]['node']
            else:
                pre = my_gragh[point[1]]['node']
            pre.next.append(current)
        queue = []
        for x in my_gragh:  #找入口
            if my_gragh[x]['no_pre']:
                queue.append(my_gragh[x]['node'])
        if len(my_gragh) < numCourses:  #没有前置的课可以直接学
            for i in range(numCourses):
                if i not in my_gragh:
                    ans.append(i)
        while len(queue) > 0:   #BFS
            now = queue.pop(0)
            for node in now.next:
                queue.append(node)
            if now.val not in ans:
                ans.append(now.val)
        return ans

def main():
    test = Solution()
    classes = [[0,1],[0,2]]
    print(test.findOrder(4,classes))

if __name__ == '__main__':
    main()