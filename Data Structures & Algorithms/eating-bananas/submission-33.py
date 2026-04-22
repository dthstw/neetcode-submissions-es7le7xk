class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            print(f"new speed {m} bananas/h")
            lim = h
            for i in range(len(piles)):
                print(f'hours required for {i+1}st pile: {(piles[i] + m - 1) // m}')
                lim -= (piles[i] + m - 1) // m
            print(f'hours still left: {lim}')  
            if lim >= 0:
                r = m - 1
                print(f"thus right pointer became {r} bananas/h")
            else:
                l = m + 1
                print(f"thus left pointer became {l} bananas/h")

        return l
        #piles=[3,6,7,11] h=8
        # 1) m = 6 -> lim = 8 8-=