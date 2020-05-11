class Solution:
    def reverseWords(self, s: str) -> str:
        temp = list(reversed(s.strip().split(" ")))
        while True:
            try:
                temp.remove("")
            except ValueError:
                break
        return " ".join(temp)


def main():
    test = Solution()
    print(test.reverseWords("hello world!"))

if __name__ == '__main__':
    main()