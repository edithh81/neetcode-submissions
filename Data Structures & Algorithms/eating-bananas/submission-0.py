import math 


class Solution:
    def canFinish(self, piles: List[int], h: int, speed: int) -> bool:
        total_hour = 0
        for pile in piles:
            total_hour += math.ceil(pile / speed)

        return total_hour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h: number of hours you have to eat all the bananas
        piles.sort()
        # piles -> number of bananasa in the i_{th} pile
        l = 1
        r = max(piles)

        while (l < r):
            m = (l + r) // 2
            if self.canFinish(piles, h, m):
                r = m
            else:
                l = m + 1
        return l
                
            
