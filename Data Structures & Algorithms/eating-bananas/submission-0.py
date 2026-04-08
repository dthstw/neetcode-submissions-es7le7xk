class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #самая медленная скорость которая нужна коке это самый большой пайл
        # умноженны на связку то есть max(piles)
        # ну а минимум можно поставить просто h // len(piles) 
        # min_speed, max_speed = 1, max(piles)
        # mid_speed = (max_speed + min_speed) // 2

        # all_bananas = 0
        # for pile in piles:
        #     all_bananas += pile

        # def hours_needed(speed):
        #     while h >= 0:
        #         all_bananas -= speed
        #         h -= 1
        #     if all_banas 

        # while min_speed <= max_speed:
        #     if mid_speed > all_bananas // h:
        #         min_speed = mid_speed
        #     elif mid_speed < all_bananas // h:
        #         max_speed = mid_speed - 1
        #     else:
        #         mid_speed

        min_speed, max_speed = 1, max(piles)
        res = max_speed
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid_speed)
            if h >= hours:
                res = min(res, mid_speed)
                max_speed = mid_speed - 1
                
            else:
                min_speed = mid_speed + 1


        return res

        
