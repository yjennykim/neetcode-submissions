class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # return number of car fleets

        data = [(position[i], speed[i]) for i in range(len(position))]
        data.sort()
        st = [] # monotonic increasing stack => number fleets

        for pos, sp in data:
            
            # pos + speed(time) = target
            time = (target - pos) / sp 
            while st and time >= st[-1]:
                st.pop()
            st.append(time)
        
        return len(st)

            


