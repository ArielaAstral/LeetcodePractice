
class Node:
    def __init__(self):
        self.char=[None]*26
        self.bool=False
class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        temp=self.root
        for letter in word:
            index=ord(letter)-ord('a')
            if temp.char[index]==None:
                temp.char[index]=Node()
            temp=temp.char[index]
        temp.bool=True

    
    def search(self, word: str) -> bool:
        temp=self.root
        for letter in  word:
            index=ord(letter)-ord('a')
            if temp.char[index]==None:
                return False
            else:
                temp=temp.char[index]
        return temp.bool
    def startsWith(self, prefix: str) -> bool:
        temp=self.root
        for letter in  prefix:
            index=ord(letter)-ord('a')
            if temp.char[index]==None:
                return False
            else:
                temp=temp.char[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
