#简单粗暴，时间复杂度O(n^2)，最后两个测试用例超时。。
import time


def main():
    stime = time.time()
    test = Solution()
    num = [[14, 15, 100, 9, 3], [32, 1, 9, 3, 5], [15, 29, 2, 6, 8, 7], [7, 10]]
    list1 = test.computeSimilarities(num)
    etime = time.time()
    print(list1)
    print(etime-stime)

class Solution:
    def computeSimilarities(self, docs):
        list_result = []
        for i in range(len(docs)):
            for j in range(i,len(docs)):
                str1 = ""
                temp = len(list(set(docs[i]).intersection(set(docs[j]))))
                if(temp==0 or i==j):continue
                list_result.append(f'{i},{j}: {temp/len(list(set(docs[i]).union(set(docs[j])))) + 1e-9:.4f}')
        return list_result










if __name__ == '__main__':
    main()