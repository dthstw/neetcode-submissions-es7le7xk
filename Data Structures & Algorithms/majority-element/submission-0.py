class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashM = defaultdict(int)

        for idx in range(len(nums)):
            hashM[nums[idx]] += 1
            if hashM[nums[idx]] > len(nums)//2:
                return nums[idx]

            
