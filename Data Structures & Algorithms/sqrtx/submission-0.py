class Solution:
    def mySqrt(self, x: int) -> int:
        # что такое корень это x=9 => root^2=x => root * root = x
        low, high = 0, x
        while low <= high: 
            mid = low + (high - low) // 2
            if mid*mid < x:
                low = mid + 1
            elif mid*mid > x:
                high = mid - 1
            else: 
                return mid
        return high