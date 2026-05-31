class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total % 2 != 0:
            print("returning")
            return False
        
        for num in nums:
            if num > target:
                return False

        numSet = set()
        numSet.add(0)

        for num in nums:
            for existingNum in list(numSet):
                numSet.add(num + existingNum)
                numSet.add(num)
                if target in numSet:
                    return True
        
        return False


