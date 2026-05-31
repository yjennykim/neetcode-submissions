class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
    
class PrefixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
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
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        if '0' not in node.children:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return True
        