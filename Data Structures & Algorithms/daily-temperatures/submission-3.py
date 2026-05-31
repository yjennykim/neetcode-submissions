class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        
        """
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while len(stack) > 0 and temp > stack[-1][0]:
                oldVal, oldIndex = stack.pop()
                res[oldIndex] = i - oldIndex
        
            stack.append((temp, i))
        
        return res


