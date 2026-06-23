class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        st = []
        for c in s:
            is_opening = (c in mapping)
            if is_opening: 
                st.append(mapping[c])
            else:
                if not st:
                    return False

                closing = st.pop()
                if c != closing:
                    return False
        
        if st:
            return False
        return True

