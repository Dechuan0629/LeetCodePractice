class Solution:
    def maxSumOfThreeSubarrays(self, nums: list, k: int) -> list:
        sumSubArrayList = []
        for i in range(len(nums)-k+1):
            subArraySum = sum(nums[i:i+k])
            sumSubArrayList.append([i,subArraySum])
        sumSubArrayList.sort(key = lambda x : x[1],reverse=True)
        print(sumSubArrayList)
        ans = []
        maxSum = 0
        for i in range(len(sumSubArrayList)):
            tempSum = 0
            tempList = []
            tempCount = 1
            tempSum += sumSubArrayList[i][1]
            indexI = sumSubArrayList[i][0]
            tempList.append(indexI)
            for j in range(i+1,len(sumSubArrayList)):
                indexJ = sumSubArrayList[j][0]
                if indexJ < indexI-k+1 or indexJ > indexI+k-1:
                    tempSum += sumSubArrayList[j][1]
                    tempCount += 1
                    tempList.append(indexJ)
                    for m in range((j+1),len(sumSubArrayList)):
                        indexM = sumSubArrayList[m][0]
                        if (indexM < indexI-k+1 or indexM > indexI+k-1) and (indexM < indexJ-k+1 or indexM > indexJ+k-1):
                            tempSum += sumSubArrayList[m][1]
                            tempCount += 1
                            tempList.append(indexM)
                            break
                    if tempCount == 3 and tempSum > maxSum:
                        maxSum = tempSum
                        ans = [] + tempList
                    else:
                        tempList.pop()
                        tempCount -= 1
                        tempSum -= sumSubArrayList[j][1]
        return sorted(ans)


def main():
    test = Solution()
    nums = [17,9,3,2,7,10,20,1,13,4,5,16,4,1,17,6,4,19,8,3]
    #未解决
    print(test.maxSumOfThreeSubarrays(nums,4))


if __name__ == '__main__':
    main()