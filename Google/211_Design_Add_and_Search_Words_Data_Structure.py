class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)

    def dfs(self, word: str, s: int, node: TrieNode) -> bool:
        if s == len(word):
            return node.isWord
        if word[s] != '.':
            next_node = node.children[ord(word[s]) - ord('a')]
            return next_node and self.dfs(word, s + 1, next_node)
        
        # If word[s] == '.', then search all the 26 children.
        for i in range(26):
            if node.children[i] and self.dfs(word, s + 1, node.children[i]):
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
