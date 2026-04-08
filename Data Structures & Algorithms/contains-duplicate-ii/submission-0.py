class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashT = {}
        
        for i, n in enumerate(nums):
            if n in hashT:
                if i - hashT[n] <= k:
                    return True
            
            hashT[n] = i
        return False
        
