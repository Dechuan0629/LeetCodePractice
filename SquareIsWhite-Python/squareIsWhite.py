class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ((ord(coordinates[0]) - 96) % 2 == 0) != (int(coordinates[1]) % 2 == 0)

def main():
    test = Solution()
    print(test.squareIsWhite("a5"))

if __name__ == '__main__':
    main()