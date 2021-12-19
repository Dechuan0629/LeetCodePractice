class Solution:
    def findJudge(self, n: int, trust: list) -> int: #暴力解法，此题应应用有向图概念
        peoples = {}
        count = 0
        for people in trust:
            if people[0] in peoples:
                peoples[people[0]].append(people[1])
            else:
                peoples[people[0]] = [people[1]]
                count +=1
        if count != n-1:
            return -1
        if len(peoples) == 0:
            return 1
        ans = []
        index = 0
        for value in peoples.values():
            if index == 0:
                ans+=value
            else:
                ans = [val for val in ans if val in value]
            index+=1
        if len(ans) != 1:return -1
        if ans[0] in peoples:return -1
        else:return ans[0]

def main():
    test = Solution()
    trust = []
    print(test.findJudge(1,trust))

if __name__ == '__main__':
    main()