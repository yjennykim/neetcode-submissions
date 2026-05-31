class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0]) # sort by position

        fleet = 0
        prevTime = -1
        for pos, speed in reversed(cars):
            time = (target - pos) / speed

            # if i'm slower than the car behind me, then we form a fleet
            if time > prevTime:
                fleet += 1
            
                prevTime = time
            

        return fleet