from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(word):
            return word == word[::-1]
        
        def backtrack(start, current_partition):
            # If we've reached the end of the string
            if start == len(s):
                res.append(current_partition.copy())
                return
            
            # Explore all possible substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):  # Check if it's a palindrome
                    current_partition.append(substring)  # Add it to current partition
                    backtrack(end, current_partition)  # Recur on the remaining string
                    current_partition.pop()  # Backtrack

        backtrack(0, [])
        return res
