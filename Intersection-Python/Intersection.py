class Solution:
    def intersection(self, start1: list, end1: list, start2: list, end2: list) -> list: # y1=a1*x+b1,y2=a2*x+b2
        judge1,judge2 = 0,0
        try:
            a1 = float(end1[1] - start1[1]) / float(end1[0] - start1[0])       #a = y1-y0/x1-x0
        except ZeroDivisionError:
            a1 = 1
            judge1 = 1
        try:
            a2 = float(end2[1] - start2[1]) / float(end2[0] - start2[0])
        except ZeroDivisionError:
            a2 = 1
            judge2 = 1
        b1 = float(start1[1]) - a1 * start1[0]     #b = y-a*x
        b2 = float(start2[1]) - a2 * start2[0]
        if a1 == a2 and b1 != b2:  #平行但不重合的线段
            return []
        if a1 == a2 and b1 == b2:   #重合在一条直线上的线段
            length = float((max(end1[1],end2[1]) - min(start1[1],start2[1]))**2 + (max(end1[0],end2[0]) - min(start1[0],start2[0]))**2)**0.5
            length1 = float((end1[1] - start1[1])**2 + (end1[0] - start1[0])**2)**0.5
            length2 = float((end2[1] - start2[1]) ** 2 + (end2[0] - start2[0]) ** 2) ** 0.5
            if length > length1+length2:  #在一条直线上但不重合的线段
                return []
            else:
                if start1[0] == start2[0]:
                    if length == length1:    #防止出现反方向的情况
                        return [start1[0],start1[1]]
                    elif length == length2:
                        return [start2[0],start2[1]]
                    return [float(min(end1[1],end2[1])-b1)/a1,min(end1[1],end2[1])]
                elif end1[0] == end2[0]:
                    return [float(min(start1[1],start2[1])-b1)/a1,min(start1[1],start2[1])]
                else:
                    return [float(max(start1[0],start2[0])),float(max(start1[0],start2[0]))*a1+b1]
        #交点 x = (b2-b1)/(a1-a2),将x带回得到y
        x = (b2-b1)/(a1-a2)
        if judge1 == 1:            #judge用于判断两条线段是否有垂直于x轴的，如果有，x的赋值方法需要改变
            x = 0-b1
            y = a2*x+b2
        elif judge2 == 1:
            x = 0-b2
            y = a1*x+b1
        else:
            y = a1*x+b1
        if x >= min(start1[0],end1[0]) and x <= max(start1[0],end1[0]) and x >= min(start2[0],end2[0]) and x <= max(start2[0],end2[0]):
            return [x,y]     #只要不平行，就一定会出现重合的点，这里只需要判断重合点是否同时存在于两条线段之内
        else:
            return []


def main():
    start1,end1 = [1,0],[1,1]
    start2,end2 = [-1,0],[3,2]
    test = Solution()
    print(test.intersection(start1,end1,start2,end2))



if __name__ == '__main__':
    main()