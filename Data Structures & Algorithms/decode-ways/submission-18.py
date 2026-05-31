class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge cases
        if len(s) == 0 or s[0] == '0': 
            return 0
        
        # If the string is of length 1, it's either valid or invalid depending on the character.
        if len(s) == 1:
            return 1

        # Initialize the dp array, with two base cases.
        ways = [0] * len(s)
        ways[0] = 1  # There is 1 way to decode the first character if it's not '0'.
        
        # For the second character
        if s[1] != '0':
            ways[1] = ways[0]  # You can always decode the second character alone.
        
        # Check if the first two characters form a valid two-digit number (between '10' and '26').
        if '10' <= s[:2] <= '26':
            ways[1] += 1  # If it's a valid number, you can also decode it as a two-digit number.

        # Fill the dp array for the rest of the string.
        for i in range(2, len(s)):
            if s[i] != '0':
                ways[i] += ways[i-1]  # Single digit decoding
            
            if '10' <= s[i-1:i+1] <= '26':  # Check the last two characters.
                ways[i] += ways[i-2]
        
        return ways[-1]
class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge cases
        if len(s) == 0 or s[0] == '0': 
            return 0
        
        # If the string is of length 1, it's either valid or invalid depending on the character.
        if len(s) == 1:
            return 1

        # Initialize the dp array, with two base cases.
        ways = [0] * len(s)
        ways[0] = 1  # There is 1 way to decode the first character if it's not '0'.
        
        # For the second character
        if s[1] != '0':
            ways[1] = ways[0]  # You can always decode the second character alone.
        
        # Check if the first two characters form a valid two-digit number (between '10' and '26').
        if '10' <= s[:2] <= '26':
            ways[1] += 1  # If it's a valid number, you can also decode it as a two-digit number.

        # Fill the dp array for the rest of the string.
        for i in range(2, len(s)):
            if s[i] != '0':
                ways[i] += ways[i-1]  # Single digit decoding
            
            if '10' <= s[i-1:i+1] <= '26':  # Check the last two characters.
                ways[i] += ways[i-2]
        
        return ways[-1]
