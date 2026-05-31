class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0]) # sort by position

        fleet = 0
        prevSpeed = 101
        prevTime = 0
        for pos, speed in reversed(cars):  # Iterate from the back
            time = (target - pos) / speed
            if time > prevTime:  # A new fleet is formed
                fleet += 1
                prevTime = time  # Update prevTime to the current car's time

        return fleet