class Solution:
    def maximalSquare(self, matrix: list) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':   #动态规划，转移方程为dp[i][j] = min(dp[i−1,j],dp[i−1,j−1],dp[i,j−1)]+1,因为如果其三个方向上有一个为0，则证明不是正方形，则得不到更新
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

    # 暴力法，用全1卷积核对每一个点做卷积，如果存在与当前卷积核面积相等的点，则证明有这个正方形存在，找出最大的即可，leetcode超时
    # from scipy import signal
    # def maximalSquare(self, matrix: list) -> int:
    #     temp = []
    #     ans = 0
    #     for line in matrix:
    #         temp.append(list(map(int,line)))
    #     for i in range(min(len(matrix),len(matrix[0]))):
    #         kernel = [[1] * (i+1) for _ in range(i+1)]
    #         check = signal.convolve2d(temp, kernel, mode='valid')
    #         if (i+1)*(i+1) in check:
    #             ans = max(ans,(i+1)*(i+1))
    #     return ans

def main():
    test = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]
    print(test.maximalSquare(matrix))


if __name__ == '__main__':
    main()