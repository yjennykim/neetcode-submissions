class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for c in s:
            if c in mapping: # if opening 
                stack.append(mapping[c]) 
            else:
                if len(stack) == 0 or stack.pop() != c:
                    return False
        
        return len(stack) == 0

        