import queue
class Solution:
    def maxDistance(self, grid: list) -> int:             #从陆地开始，总体利用广度优先的思想，最后一个搜索到的海洋便是最远的
        x_direction = [-1,1,0,0]                    #也可以从海洋开始进行bfs，找到第一个也就是最近的陆地便终止，记录距离，最后返回距离的最大值
        y_direction = [0,0,-1,1]
        land = [[x, y] for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y]]  #得到所有陆地的坐标
        if len(land) == 0 or len(land) == len(grid)*len(grid[0]):  #如果全是海洋或者全是陆地便返回-1
            return -1
        land_queue = queue.Queue()
        for [x,y] in land:                                #同时利用多源bfs，同时进行搜索，因为会对搜索过的地点标记，因此一定可以同时搜索到最远距离
            land_queue.put([x,y])
        while not land_queue.empty():
            x_now,y_now = land_queue.get()
            for i in range(4):                            #对每一个方向搜索、入队
                dx = x_now+x_direction[i]
                dy = y_now+y_direction[i]
                if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy]!=0:
                    continue
                grid[dx][dy] = grid[x_now][y_now]+1  # 通过对点值的累加，得到到源点的距离，同时可以防止重复访问
                land_queue.put([dx,dy])
        return grid[x_now][y_now] - 1                #因为第一个距离会从2开始，所以最终的距离需要减1


def main():
    test =Solution()
    grid = [[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]]
    for line in grid:
        print(line)
    print(test.maxDistance(grid))


if __name__ == '__main__':
    main()