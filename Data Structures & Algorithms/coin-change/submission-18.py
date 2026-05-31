class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # can't do % with // since by taking the largest coin, might be ignoring better combinations
        if not coins:
            return -1
        
        if amount == 0:
            return 0

        nums = [math.inf for _ in range(amount + 1)]
        for num in coins:
            if num <= amount:
                nums[num] = 1
        nums[0] = 0

        for i in range(amount + 1): 
            for coin in coins:
                if coin + i <= amount:
                    nums[coin+i] = min(nums[coin + i], nums[i] + 1)

        return nums[amount] if nums[amount] != math.inf else -1

                
        