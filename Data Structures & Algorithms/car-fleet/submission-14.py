class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [(position[i], speed[i]) for i in range(len(position))]
        data.sort()

        st = []
        for car_pos, car_speed in data:
            car_time = (target - car_pos) / car_speed
            
            # i'm taking longer than previous car
            while st and car_time >= st[-1]:
                st.pop()
            
            st.append(car_time)
            
        return len(st)
