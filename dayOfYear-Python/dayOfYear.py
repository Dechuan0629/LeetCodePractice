class Solution:
    def dayOfYear(self, date: str) -> int:
        leap = {"01":0,"02":31,"03":60,"04":91,"05":121,"06":152,"07":182,"08":213,"09":244,"10":274,"11":305,"12":335}
        unLeap = {"01":0,"02":31,"03":59,"04":90,"05":120,"06":151,"07":181,"08":212,"09":243,"10":273,"11":304,"12":334}
        year,month,day = date.split("-")
        if self.isLeap(int(year)):return leap[month] + int(day)
        else:return unLeap[month] + int(day)

    def isLeap(self,year:int) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


def main():
    test = Solution()
    print(test.dayOfYear("1900-03-01"))

if __name__ == '__main__':
    main()