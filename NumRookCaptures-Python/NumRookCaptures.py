import numpy as np

class Solution:
    def numRookCaptures(self, board: list) -> int:
        count = 0
        index1 = -1
        for index,list1 in enumerate(board):   #找到 车 的下标
            try:
                index1 = list1.index("R")
            except ValueError:
                continue
            else:
                break
        if index1 == -1:return -1
        array = np.array(board)
        print(array)
        raw = array[index].tolist()              #提取出车所在的行和列
        column = array[:,index1].tolist()
        up,low,left,right,stop_up,stop_low,stop_left,stop_right = index,index,index1,index1,0,0,0,0
        while(True):
            if stop_up == 1 and stop_low == 1 and stop_left == 1 and stop_right == 1:break       #上下左右皆已经找到或没找到或走到边界了便终止
            up-=1
            low+=1
            left-=1
            right+=1
            if(up>=0 and stop_up==0):
                if column[up] == 'p':
                    count+=1
                    stop_up = 1
                elif column[up] == 'B':stop_up = 1
            else:stop_up = 1

            if(low<len(column) and stop_low==0):
                if column[low] == 'p':
                    count+=1
                    stop_low = 1
                elif column[low] == 'B':stop_low = 1
            else:stop_low = 1

            if(left>=0 and stop_left==0):
                if raw[left] == 'p':
                    count+=1
                    stop_left = 1
                elif raw[left] == 'B':stop_left = 1
            else:stop_left = 1

            if(right<len(raw) and stop_right==0):
                if raw[right] == 'p':
                    count+=1
                    stop_right = 1
                elif raw[right] == 'B':stop_right = 1
            else:stop_right = 1
        return count

def main():
    test = Solution()
    list1 = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(test.numRookCaptures(list1))

if __name__ == '__main__':
    main()