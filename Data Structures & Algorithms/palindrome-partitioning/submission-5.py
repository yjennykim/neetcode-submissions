class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        substrings = []
        
        def checkPalindrome(word):
            return word[::-1] == word

        def recurse(i):
            if i >= len(s):
                res.append(substrings.copy())
                return
            
            for j in range(i, len(s)):
                if checkPalindrome(s[i:j+1]):
                    substrings.append(s[i:j+1])
                    recurse(j+1)
                    substrings.pop()

        recurse(0)
        return res

# aab 
# 

