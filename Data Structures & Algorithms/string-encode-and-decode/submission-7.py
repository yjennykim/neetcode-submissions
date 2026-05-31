class Solution:

    def encode(self, strs: List[str]) -> str:
        build = ""
        for st in strs:
            build += str(
                str(len(st)) + '#' + st
            )
        return build
        # [hello, jenny]
        # 15#hellojenny2#hi

    def decode(self, s: str) -> List[str]:
        print("decoding", s)
        res = []
        i,j = 0,0
        while j < len(s):
            while s[j] != '#':
                j += 1
            
            size = int(s[i:j])
            print("size", size)

            i = j + 1
            end_of_str_index = int(i+size)
            print("appending", s[i:end_of_str_index])
            res.append(s[i:end_of_str_index])
            i = j = end_of_str_index

        return res


            
