class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                createdNode = Node(c)
                node.children[c] = createdNode # insert character
                node = createdNode

        node.children['0'] = Node('0') # mark end

    def search(self, word: str) -> bool:
        word = word + "0"

        def dfs(prevNode, i):
            if i >= len(word):
                return True
            
            c = word[i]
            if c in prevNode.children:
                if dfs(prevNode.children[c], i+1):
                    return True
            
            elif word[i] == '.':
                for ch in prevNode.children:
                    if dfs(prevNode.children[ch], i+1):
                        return True
            
            return False
        
        return dfs(self.root, 0)

                
            
    