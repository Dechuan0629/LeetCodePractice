class Solution:
    def intToRoman(self, num: int) -> str:
        unit = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        decade = {0:"",10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
        hundred = {0:"",100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
        thousand = {0:"",1000:"M",2000:"MM",3000:"MMM"}
        return thousand[num//1000*1000] + \
               hundred[(num-num//1000*1000)//100*100] + \
               decade[(num-num//1000*1000-(num-num//1000*1000)//100*100)//10*10] + \
               unit[num%10]

def main():
    test = Solution()
    print(test.intToRoman(777))

if __name__ == '__main__':
    main()