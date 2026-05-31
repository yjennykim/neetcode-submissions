class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []

        count = {}

        for i in range(len(s)):
            # map letter to final index
            count[s[i]] = i
        print(count)
        
        res = []
        start = 0
        end = count[s[0]]
        while end < len(s):
            i = start
            while i <= end:
                end = max(count[s[i]], end)
                i += 1

            res.append(end - start + 1)
            start = end + 1
            if start >= len(s):
                return res

            end = count.get(s[start])

        return res