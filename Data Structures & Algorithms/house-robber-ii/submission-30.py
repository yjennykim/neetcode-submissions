class Solution:
    def rob(self, nums: List[int]) -> int:

        def robbing(arr): 
            n = len(arr)
            if n == 0: return 0
            if n == 1: return arr[0]
            best = [0] * n
            best[0] = arr[0]
            best[1] = max(arr[0], arr[1])

            for i in range(2, n):
                best[i] = max(best[i-2] + arr[i], best[i-1])
            print("Best", best)
            return best[n-1]
        
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(robbing(nums[1:]), robbing(nums[:-1]))
        
