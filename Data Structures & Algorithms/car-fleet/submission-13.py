class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort()

        st = []
        # start with early positions
        for pos, sp in cars:
            # position + speed(time) = target
            time = (target - pos) / sp
            
            # check the car behind it. Did it catch up to me
            while st and time >= st[-1]:
                st.pop()
            
            st.append(time)
        
        return len(st)