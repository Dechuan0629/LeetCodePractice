class Solution:
    def mincostTickets(self, days: list, costs: list) -> int:
        total_cost = [0]
        i = 1
        for travel_day in days:
            for corrent_day in range(i,365+1):  #对一年中的每一天都进行模拟
                if corrent_day != travel_day:
                    total_cost.append(total_cost[corrent_day-1])   #如果不是旅游日，就不用买新的票
                    continue
                else:
                    total_cost.append(    #如果是旅游日，就看1、7、30天前买的哪种票，接下来尝试买1，7，30天的票，看哪种更便宜
                        min(total_cost[max(0,corrent_day-1)]+costs[0],
                            total_cost[max(0,corrent_day-7)]+costs[1],
                            total_cost[max(0,corrent_day-30)]+costs[2]
                        )
                    )
                    break
            i = corrent_day+1
        print(total_cost)
        return total_cost[days[-1]]

def main():
    test = Solution()
    days = [1,2,3,8,11,19,37,38,39,40,51,102,113,115,119,120,180,250,361,362,363,364,365]
    cost = [2,7,15]
    print(test.mincostTickets(days,cost))


if __name__ == '__main__':
    main()