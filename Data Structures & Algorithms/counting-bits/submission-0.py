class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            count = 0

            temp = i
            while temp != 0:
                if temp & 1 == 1:
                    count += 1
                temp >>= 1

            res[i] = count
        return res