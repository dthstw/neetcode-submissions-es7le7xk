class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1
        
        while l < r:
            remainder = target - numbers[l]
            if remainder > numbers[r]:
                l += 1
            elif remainder < numbers[r]:
                r -= 1 
            else:
                return [l + 1, r + 1]