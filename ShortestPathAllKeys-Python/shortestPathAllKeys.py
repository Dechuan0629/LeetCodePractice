import queue
class Solution:
    def shortestPathAllKeys(self, grid: list) -> int:
        #先遍历数组，找出钥匙的数量和起始位置
        keyCounts = 0
        startIndexRow = 0
        startIndexCol = 0
        for i,row in enumerate(grid):
            for j,element in enumerate(row):
                if ord(element) >= 97 and ord(element) <= 122:
                    keyCounts += 1
                if element == "@":
                    startIndexRow = i
                    startIndexCol = j
        if keyCounts == 0: return -1
        x_direction = [-1,1,0,0]
        y_direction = [0,0,-1,1]
        location = queue.Queue()
        location.put([startIndexRow,startIndexCol,0])
        keysBag = {}
        minDis = 99999
        step = 0
        #通过bfs算法，获取到各钥匙点之前的距离
        while not location.empty():
            x_now,y_now,distance = location.get()
            #遇到钥匙，放进包里
            if ord(grid[x_now][y_now]) >= 97 and ord(grid[x_now][y_now]) <= 122:
                keysBag[grid[x_now][y_now]] = 1
            #钥匙找齐了，找出最短距离
            if len(keysBag) == keyCounts:
                minDis = min(minDis,distance)
            grid[x_now] = grid[x_now][:y_now] + "!" + grid[x_now][y_now + 1:]
            for i in range(4):                            #对每一个方向搜索、入队
                dx = x_now+x_direction[i]
                dy = y_now+y_direction[i]
                #到达边界，停止、遇到墙，停止、遇到旗，停止
                if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy] == "#" or grid[dx][dy] == "!":
                    continue
                #遇到锁，查看背包里有没有对应的钥匙
                if ord(grid[dx][dy]) >= 65 and ord(grid[dx][dy]) <= 90:
                    if keysBag.get(chr(ord(grid[dx][dy])+32)) == None:
                        continue
                distance_new = distance + 1
                location.put([dx,dy,distance_new])
        return minDis if minDis != 99999 else -1
#基本思路：枚举法
#利用广度优先遍历，获取各钥匙点之间的距离
#找出从起点开始，能到达所有点的最短路径
def main():
    test = Solution()
    keyMap = ["@...a",".###A","b.BCc"]
    for row in keyMap:
        print(row)
    print("------")
    print(test.shortestPathAllKeys(keyMap))

if __name__ == '__main__':
    main()