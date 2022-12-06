class Solution:
    def boxDelivering(self, boxes, portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # 假设对于boxes[i]，总步数为d[i]
        # 显然对于d[i]有三种情况，同一港口、不同港口、回家，对应d[i] = d[i-1] + (0 or 1 or 2)
        # 0、同一港口：port(i-1) == port(i) and sumWeight(i-1) + weight(i) <= maxWeight and sumBox(i-1) + 1 <= maxBoxes
        # 1、不同港口：i == 0 or (port(i-1) != port(i) and sumWeight(i-1) + weight(i) <= maxWeight and sumBox(i-1) + 1 <= maxBoxes) or i == len(boxes)
        # 2、回家：sumWeight(i-1) + weight(i) > maxWeight or sumBox(i-1) + 1 > maxBoxes
        # in condition 0 and 1：sumWeight(i) = sumWeight(i-1) + weight(i)，sumBox(i) = sumBox(i-1) + 1
        # in condition 2：sumWeight(i) =  weight(i)，sumBox(i) = 1
        # 本题就是要找到最小的step，但是这种情况下局部最小，并不一定能达到全局最小（贪心算法）
        # 对于最优情况，当然是出现c0的次数越多越好，其次是c1，最后是c2
        # 反过来说，c2出现的次数越少越好，其次是c1，最后是c0
        # 但是如果我们直接按上述情况进行解题，就成了贪心算法：每次都尽最大努力往车上装货
        # 不难发现，max(c0)可以等价于min(c2)，min(c0)可以等价于max(c2)
        # 也就是说，我们在满足max(c0)或min(c2)的情况下，都可以保证全局最优
        # 在本题内，c0和c1可以看作一种情况--在车上，c2是另一种情况--回家
        # 因此如果按照贪心算法的思路，c0和c1需为不同的情况，使得我们安排车上货物时，按照权重c0 > c1 > c2去处理，但此题实际上c0 = c1 > c2
        # 所以此题我们需要反过来，按照min(c2)的情况去做，就能达到全局最优解
        # 对于boxes[i]如果为c0，那么可以直接装车，不用考虑
        # 对于boxes[i]为c1，此时需要选择装还是不装
        # 因为对于后续情况是未知的，所以此时需要走入到两种情况，装|不装
        # 那么对于dc1[i]有d[i]=min(dc1:+1,dc2:+2)->递归
        return self.pack(boxes, maxBoxes, maxWeight, 0, 0, 0)

    def pack(self, boxes, maxBoxes, maxWeight, sumWeight, sumBoxes, index) -> int:
        if index >= len(boxes):
            return 1
        # 如果为c1，需要获取min(装车，不装车)
        if index == 0 or (boxes[index][0] != boxes[index - 1][0] and sumWeight + boxes[index][
            1] <= maxWeight and sumBoxes + 1 <= maxBoxes):
            print("装车还是回家？")
            pack = self.pack(boxes, maxBoxes, maxWeight, sumWeight + boxes[index][1], sumBoxes + 1, index + 1)
            unpack = self.pack(boxes, maxBoxes, maxWeight, boxes[index][1], 1, index + 1)
            return 1 + pack if pack <= unpack else 2 + unpack
        # c0，直接装车
        elif boxes[index][0] == boxes[index - 1][0] and sumWeight + boxes[index][
            1] <= maxWeight and sumBoxes + 1 <= maxBoxes:
            print("装车！")
            return self.pack(boxes, maxBoxes, maxWeight, sumWeight + boxes[index][1], sumBoxes + 1, index + 1)
        # c2，直接装车
        else:
            print("回家！")
            return 2 + self.pack(boxes, maxBoxes, maxWeight, boxes[index][1], 1, index + 1)

#失败！O（n^2）超时
def main():
    test = Solution()
    boxes = [[48,52899],[47,19850],[33,29679],[69,33222],[58,701],[30,76794],[25,81170],[73,23227],[55,20126],[44,36120],[45,31939],[67,19736],[68,38178],[17,83260],[38,15272],[38,78703],[35,17238],[75,18299],[8,20643],[23,49506],[64,11294],[57,52676],[50,72049],[18,62783],[72,47322],[58,17174],[33,91245],[41,20540],[9,52226],[8,56422],[38,67101],[55,84871],[10,22701],[13,65749],[10,75225],[27,13437],[5,82776],[53,69170],[40,19975],[71,52129],[56,92827],[77,91290],[34,52128],[49,42076],[65,14024],[11,20086],[54,72018],[64,64707],[43,53637],[18,81304],[34,769],[33,7418],[60,1473],[44,16057],[45,81799],[50,91388],[2,88844],[50,19037],[50,24485],[2,79102],[3,34503],[49,89167],[18,18198],[30,76362],[61,51312],[53,25332],[53,85378],[43,31053],[74,8190],[55,22288],[56,48727],[66,45387],[12,53165],[46,66319],[48,47049],[34,4879],[20,35950],[27,80365],[59,42479],[50,17398],[63,26273],[27,78622],[57,27062],[16,53519],[42,31522],[39,26623],[35,71692],[33,72780],[23,17746],[2,939],[47,3748],[63,71487],[25,92114],[58,48662],[24,45749],[64,63233],[26,92359],[29,11382],[58,785],[59,11024],[60,55275],[50,66923],[10,6771],[61,31311],[76,61562],[69,22497],[29,24471],[43,90635],[38,40760],[64,87184],[7,19793],[47,47690],[69,9570],[39,16271],[75,87064],[26,26233],[53,69585],[29,68502],[37,16523],[34,10484],[22,88729],[31,80116],[10,17864],[33,47739],[53,67300],[21,68588],[69,58835],[75,79944],[76,13923]]
    portsCount,maxBoxes,maxWeight = 77,17,93070
    print(test.boxDelivering(boxes,portsCount,maxBoxes,maxWeight))

if __name__ == '__main__':
    main()