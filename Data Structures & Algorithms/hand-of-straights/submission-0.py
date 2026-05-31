class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # return if len(hand) not multiple of groupSize
        if len(hand) % groupSize != 0:
            return False

        if len(hand) == 0: 
            return True

        # create a map from number --> count
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        # while map is not empty,
        while len(count) > 0:
            largest = max(list(count.keys()))

            for i in range(groupSize):
                # if exists n, n-1, n-2, n-groupSize does not exist, return False.
                if largest-i not in count:
                    return False
                    
                # else, decrement respective counts 
                count[largest-i] -= 1
                # remove if count is zero
                if count[largest-i] == 0:
                    del count[largest-i]
                
            
            print("starting num", largest)
        
        # return True
        return True

"""



"""
        