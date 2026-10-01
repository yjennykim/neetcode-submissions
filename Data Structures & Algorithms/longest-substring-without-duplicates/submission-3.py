class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a window which is the substring without duplicate characters
        # everytime we explore a new letter, remove that character from window
        # maintain a longest substring counter

        longest_substring_ct = 0
        L = 0
        window = set()
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            longest_substring_ct = max(longest_substring_ct, len(window))
        
        return longest_substring_ct

            
