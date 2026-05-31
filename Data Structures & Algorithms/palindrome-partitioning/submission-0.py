from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substrings = []
        
        def checkPalindrome(word):
            return word == word[::-1]

        def recurse(start):
            if start >= len(s):
                res.append(substrings.copy())
                return

            for end in range(start + 1, len(s) + 1):
                current_substring = s[start:end]
                if checkPalindrome(current_substring):
                    substrings.append(current_substring)  # Add valid palindrome
                    recurse(end)  # Recurse for the next part
                    substrings.pop()  # Backtrack

        recurse(0)  # Start the recursion from the beginning of the string
        return res
