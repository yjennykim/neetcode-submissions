class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        differences = []
        maxIndex, maxDifference = 0, gas[0] - cost[0]
        for i in range(len(gas)):
            difference = gas[i] - cost[i] 
            differences.append(difference)
            if gas[i] - cost[i] > maxDifference:
                maxIndex = i
                maxDifference = difference
        
        if sum(differences) < 0:
            return -1

        print(differences)
        running_total = 0
        start_index = 0
        for i in range(start_index, len(differences)):
            index = i % len(differences)
            running_total += differences[index]
            if running_total < 0:
                # reset
                start_index = i + 1
                running_total = 0

        return start_index
        