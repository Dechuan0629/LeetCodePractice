class Solution:
    def exist(self, board: list, word: str) -> bool:
        self.step = len(word)
        self.word = word
        self.row, self.column = len(board), len(board[0])
        for i in range(self.row):   #深度优先遍历
            for j in range(self.column):
                if board[i][j] != word[0]:
                    continue
                self.judge = False
                self.DFS(i, j, 1, [line[:] for line in board])
                if self.judge:
                    return True
        return False

    def DFS(self, i, j, step, board):
        if i < 0 or i >= self.row or j < 0 or j >= self.column or board[i][j] == -1 or board[i][j] != self.word[
            step - 1]:
            return 0
        elif step == self.step:
            self.judge = True
            return 1
        board[i][j] = -1
        self.DFS(i - 1, j, step + 1, [line[:] for line in board])
        self.DFS(i + 1, j, step + 1, [line[:] for line in board])
        self.DFS(i, j - 1, step + 1, [line[:] for line in board])
        self.DFS(i, j + 1, step + 1, [line[:] for line in board])

def main():
    test = Solution()
    s = "ABCESEEEFS"
    matrix = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    for line in matrix:
        print(line)
    print(test.exist(matrix,s))


if __name__ == '__main__':
    main()