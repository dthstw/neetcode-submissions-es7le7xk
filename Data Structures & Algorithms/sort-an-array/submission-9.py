class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(ARR, L, M, R):
            left_part = ARR[L:M+1]
            right_part = ARR[M+1:R+1]
            i = j = 0
            k = L
            while i < len(left_part) and j < len(right_part):
                if left_part[i] >= right_part[j]:
                    ARR[k] = right_part[j]
                    j += 1
                else:
                    ARR[k] = left_part[i]
                    i += 1
                k += 1
            
            while i < len(left_part):
                ARR[k] = left_part[i]
                i += 1
                k += 1
            while j < len(right_part):
                ARR[k] = right_part[j]
                j += 1
                k += 1
            return ARR
            
            

        def MergeSort(l, r, arr):
            if l == r:
                return arr
            
            m = l + (r - l) // 2
            MergeSort(l, m, arr)
            MergeSort(m + 1, r, arr)
            return merge(arr, l, m, r)
        return MergeSort(0, len(nums) - 1, nums)