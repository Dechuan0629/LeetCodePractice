import re
class Solution:
    def decodeString(self, s: str) -> str: #正则表达式
        while '[' in s:
            s = re.sub(r'(\d+)\[([A-Za-z]*)\]', self.Conpose, s)    #每次会展开一个方括号内的内容，如果方括号内还有方括号则会从内到外依次展开
        return s
    def Conpose(self,matched):
        return int(matched.group(1)) * matched.group(2)  # group1为(\d+)表示数字倍数，group2为[([A-Za-z]*)\]表示方括号内的内容

def main():
    test = Solution()
    s = "5[ac3[q4[n]]]2[xz]"
    print(test.decodeString(s))

if __name__ == '__main__':
    main()