class Solution:
    def numIslands(self, grid: list) -> int:
        count = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if int(self.grid[i][j]) == 0:
                    continue
                else:
                    count+=self.DFS(i,j)
        return count

    def DFS(self,i,j):   #典型的深度优先搜索陆地块
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or int(self.grid[i][j]) == 0:
            return 0
        self.grid[i][j] = "0"   #已经搜索过的且连通着的陆地置0，保证不会被其他独立的陆地块重复访问
        self.DFS(i-1,j)
        self.DFS(i+1,j)
        self.DFS(i,j-1)
        self.DFS(i,j+1)
        return 1

def main():
    test = Solution()
    island = [["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]]
    print(test.numIslands(island))

if __name__ == '__main__':
    main()