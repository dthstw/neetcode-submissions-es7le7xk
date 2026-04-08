class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)
        def MergeSort(l, r, nums):
            if r - l <= 1:
                return
            m = (l + r) // 2

            MergeSort(l, m, nums)
            MergeSort(m, r, nums)

            left_part = nums[l:m]
            right_part = nums[m:r]
            i = j = 0
            k = l
            #[10, 20] [3, 41]
            #[3 10 20 41]
            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    nums[k] = left_part[i]
                    i += 1
                else:
                    nums[k] = right_part[j]
                    j += 1
                k += 1
            
            while i < len(left_part):
                nums[k] = left_part[i]
                i += 1
                k += 1
            
            # Если в правой части еще что-то осталось
            while j < len(right_part):
                nums[k] = right_part[j]
                j += 1
                k += 1
        MergeSort(l, r, nums)   

        return nums
