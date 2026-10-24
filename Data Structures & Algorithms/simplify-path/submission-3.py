class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for ch in path.split("/"):
            if ch == '..':
                if st:
                    st.pop()
            elif ch == '' or ch == '.':
                continue
            else:
                st.append(ch)
            
        return '/' + '/'.join(st)