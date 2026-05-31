class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        differences = []
        for i in range(len(gas)):
            difference = gas[i] - cost[i] 
            differences.append(difference)
        
        if sum(differences) < 0:
            return -1

        running_total = 0
        start_index = 0
        for i in range(start_index, len(differences)):
            running_total += differences[i]
            if running_total < 0:
                # reset
                start_index = i + 1
                running_total = 0

        return start_index
        