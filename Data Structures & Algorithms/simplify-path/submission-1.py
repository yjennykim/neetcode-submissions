class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        print(paths)
        res = []
        for p in paths:
            if p == '..':
                if res:
                    res.pop()
            elif p == '' or p == '.':
                continue
            else:
                res.append(p)
        
        return '/' + '/'.join(res)