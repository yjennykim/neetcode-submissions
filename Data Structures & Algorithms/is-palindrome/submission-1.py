class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for i in range(len(s)):
            if s[i].isalnum():
                ns += s[i].lower()
        
        return ns[::-1] == ns
        