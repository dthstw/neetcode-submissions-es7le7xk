class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(ARR, L, M, R):
            left = ARR[L:M+1]
            right = ARR[M+1:R+1]

            i = j = 0
            k = L

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ARR[k] = left[i]
                    i += 1
                else:
                    ARR[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                ARR[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                ARR[k] = right[j]
                j += 1
                k += 1

            return ARR


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = l + (r - l) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            return merge(arr, l, m, r)
                
        return mergeSort(nums, 0, len(nums) - 1)
                

            # [10,9,1,1,1,2,3,1]
            # [10,9,1,1] [1,2,3,1]
            # [10,9,] [1,1] [1,2] [3, 1]
            # [10] [9] [1] [1] [1] [2] [3] [1]
            #