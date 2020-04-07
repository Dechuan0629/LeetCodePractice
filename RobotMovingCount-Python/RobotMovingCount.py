import numpy as np
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.matrix = np.zeros((m,n),int).tolist()
        self.global_count = 0
        self.k = k
        self.DFS(0,0)
        return self.global_count

    def DFS(self,i:int,j:int):     #典型的DFS搜索所有可以到达的位置，因为没有障碍物，所以只需要向下向右搜索即可
        if i < 0 or i >= len(self.matrix) or j < 0 or j >= len(self.matrix[0]) or self.matrix[i][j] == 1:
            return False
        num = 0
        for c1 in str(i):
            num += int(c1)
        for c1 in str(j):
            num += int(c1)
        if num > self.k:
            return False
        self.global_count+=1
        self.matrix[i][j] = 1
        self.DFS(i+1,j)
        self.DFS(i,j+1)
        return True

def main():
    test = Solution()
    print(test.movingCount(38,15,9))


if __name__ == '__main__':
    main()