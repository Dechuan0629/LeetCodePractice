import queue
class Solution:
    def updateMatrix(self, matrix: list) -> list:
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.matrix[i][j] == 0:
                    continue
                else:
                    matrix[i][j] = self.BFS(i, j)
        return matrix

    def BFS(self,i,j):
        x_drection = [-1,1,0,0]
        y_drection = [0,0,-1,1]
        temp_queue = queue.Queue()
        temp_queue.put([i,j,0])    #bfs，保存着当前坐标与到起始点的距离
        judge = 0
        while not temp_queue.empty():
            x_now,y_now,distance = temp_queue.get()
            for i in range(4):
                dx = x_now+x_drection[i]
                dy = y_now+y_drection[i]
                if dx < 0 or dx >= len(self.matrix) or dy < 0 or dy >= len(self.matrix[0]):
                    continue
                if self.matrix[dx][dy] == 0:
                    distance+=1
                    judge = 1
                    break
                else:
                    temp_queue.put([dx,dy,distance+1])
            if judge == 1:   #找到一个0直接结束循环
                break
        return distance

def main():
    matrix = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    for line in matrix:
        print(line)
    test = Solution()
    print('-----------------------------------')
    ans = test.updateMatrix(matrix)
    for line in ans:
        print(line)

if __name__ == '__main__':
    main()