class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # monotonically decreasing stack (gets smaller bottom to top)
                    # (temp, index) 
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while len(stack) > 0 and temp > stack[-1][0]:
                oldTemp, oldI = stack.pop()
                res[oldI] = i-oldI

            stack.append((temp, i))
        
        return res
        
        """
        [1,X,1]
            (35,)
            [
                (36,3)
                (38,1)
            ] 
        """