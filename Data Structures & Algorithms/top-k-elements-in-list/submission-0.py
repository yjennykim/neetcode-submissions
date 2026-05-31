class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        numToFrequency = {}
        for num in nums:
            if num not in numToFrequency:
                numToFrequency[num] = 0
            numToFrequency[num] += 1

        l = []
        for num in numToFrequency:
            l.append((num, numToFrequency[num]))

        # sort by values
        l.sort(key=lambda pair:pair[1], reverse=True)

        # get the corresponding k top keys
        res = []
        for x in l[:k]:
            res.append(x[0])
        return res