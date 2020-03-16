class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        i = 0
        temp = 0
        count = 0
        for str1 in words:
            judge = 0
            if len(str1) > len(chars):
                continue
            temp = len(list(set(str1).intersection(set(chars))))         #求两字符串的交集长度
            if temp == len(set(str1)):                                   #交集长度等于去重后的单词长度就满足条件1
                for c in list(set(str1).intersection(set(chars))):
                    if str1.count(c)>chars.count(c):                     #同时，单词中每个字母出现的次数不能大于字母表中每个字母出现的次数
                        judge = 1
                        break
                if judge == 1:
                    continue
                count+=len(str1)
        return count



def main():
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    test = Solution()
    num = test.countCharacters(words,chars)
    print(num)

if __name__ == '__main__':
    main()