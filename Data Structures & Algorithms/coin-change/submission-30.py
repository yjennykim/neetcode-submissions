class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        OPT = [math.inf] * (amount + 1)

        # base case
        OPT[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    OPT[i + coin] = min( OPT[i + coin], OPT[i] + 1 )
        
        print(OPT)

        if OPT[amount] == math.inf:
            return -1

        return OPT[amount]



