class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        temp1 = abs(rec1[2] - rec2[2])
        temp2 = abs(rec1[3] - rec2[3])
        if (temp1 == rec1[2]- rec1[0] or temp1 == rec2[2] - rec2[0]) or (temp2 == rec1[3] - rec1[1] or temp2 == rec2[3] - rec2[1]):
            return False
        if (temp1 < rec1[2] - rec1[0] and rec1[2] >= rec2[2]) or (temp1 < rec2[2] - rec2[0] and rec2[2] >= rec1[2]):
            if (temp2 < rec1[3] - rec1[1] and rec1[3] >= rec2[3]) or (temp2 < rec2[3] - rec2[1] and rec2[3] >= rec1[3]):
                return True
        return False








def main():
    rec1 = [2, 17, 6, 20]
    rec2 = [3, 8, 6, 20]
    test = Solution()
    print(test.isRectangleOverlap(rec1,rec2))







if __name__ == '__main__':
    main()