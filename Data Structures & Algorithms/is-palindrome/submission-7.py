class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l < r :
            print("tryig with l,r", l, r)
            print(s[l], s[r])
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[r].lower() != s[l].lower():
                return False
            
            l += 1
            r -= 1
            print("incrementing", l, r)

        return True
        