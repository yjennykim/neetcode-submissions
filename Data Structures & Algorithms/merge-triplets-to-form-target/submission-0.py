class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        aFound, bFound, cFound = False, False, False

        for triplet in triplets:
            a,b,c = triplet

            if a == target[0] and b <= target[1] and c <= target[2]:
                aFound = True
            
            if b == target[1] and a <= target[0] and c <= target[2]:
                bFound = True
            
            if c == target[2] and a <= target[0] and b <= target[1]:
                cFound = True
        
        return aFound and bFound and cFound