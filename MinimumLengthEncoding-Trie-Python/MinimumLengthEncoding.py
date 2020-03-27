class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.get(letter)
            if not child:
                node[letter] = {}
            node = node[letter]


class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        count = 1
        trie = Trie()
        self.global_count = 0
        for word in words:
            trie.insert(reversed(word))         #因为需要对单词的后缀进行匹配，所以这里将单词倒序输入生成字典树
        self.check_count(trie.root,count)
        return self.global_count

    def check_count(self,tree:dict,count1:int): #字典树下每一条路径都是一个完整的单词，因为是倒序输入，后缀重复出现的单词将不会占用一条到叶子节点的路径
        for temp in tree:                       #因此遍历每一条路径到叶子节点的节点数和它们的总和，即为最短可匹配的字符串长度
            count1+=1
            print(temp,count1)
            if tree[temp] == {} :
                self.global_count+=count1
            self.check_count(tree[temp],count1)
            count1-=1
        return 1

def main():
    test = Solution()
    words = ["time", "me", "bell"]
    print(test.minimumLengthEncoding(words))


if __name__ == '__main__':
    main()