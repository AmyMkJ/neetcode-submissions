class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0

        for p, s in cars:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                fleet += 1
                stack.append(time)

        return fleet 

        