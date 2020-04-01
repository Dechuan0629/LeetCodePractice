from scipy import signal
import numpy as np
class Solution:
    def gameOfLife(self, board: list) -> None:  #代码很简单，但是会耗费与board相同大小的空间存储检查表，可尝试原地算法
        kernel = [[1,1,1],
                  [1,1,1],
                  [1,1,1]]
        check = signal.convolve2d(board,kernel,mode='same') #利用3*3的全1卷积核做卷积运算可以很容易的得到每个位置周围的存活细胞数
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check[i][j] == 3 or (check[i][j] == 4 and board[i][j] == 1):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        print("After:\n",board)

def main():
    test = Solution()
    list1 = np.random.randint(0,2,(10,10))
    print("Before:\n",list1)
    test.gameOfLife(list1)



if __name__ == '__main__':
    main()