class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            nums = [5,4,6]

            numSet = {0,1}
            maxSequence = 0

            currSequence=2
            3,2,1,0,4,5,6

        """

        numSet = set(nums)
        maxSequence = 0

        while len(numSet) > 0:
            num = numSet.pop()
            currSequence = 1

            temp=num
            while temp-1 in numSet:
                currSequence += 1
                numSet.remove(temp-1)
                temp -= 1

            temp=num
            while temp+1 in numSet:
                currSequence += 1
                numSet.remove(temp+1)
                temp += 1

            maxSequence = max(maxSequence, currSequence)

        return maxSequence
        
