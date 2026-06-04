class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(houses):
            print("House", houses)
            n = len(houses)
            if n == 0: return 0
            if n == 1: return houses[0]
            if n == 2: return max(houses[0], houses[1])

            opt = [0] * n
            
            opt[0] = houses[0]
            opt[1] = max(houses[0], houses[1])

            for i in range(2, n):
                opt[i] = max(opt[i-1], opt[i-2] + houses[i])
            
            print("Opt", opt[n-1])
            return opt[n-1]

        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        return max(
            rob1(nums[:n-1]),
            rob1(nums[1:n]),
        )