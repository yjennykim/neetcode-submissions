class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        st = []
        for ch in s:
            if ch in mapping:
                st.append(mapping[ch])
            elif not st:
                return False
            elif st[-1] != ch:
                return False
            else:
                st.pop()
        
        return len(st) == 0


