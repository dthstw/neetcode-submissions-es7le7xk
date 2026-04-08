class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left_part = arr[L:M+1]
            right_part = arr[M+1:R+1]

            i = j = 0
            k = L
            while i < len(left_part) and j < len(right_part):
                if left_part[i] < right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                k += 1

            while i < len(left_part):
                arr[k] = left_part[i]
                i += 1
                k += 1
            while j < len(right_part):
                arr[k] = right_part[j]
                j += 1
                k += 1
            return arr

        def MergeSort(arr, l, r):
            if l == r:
                return arr
            m = l + (r - l) // 2

            MergeSort(arr, l, m)
            MergeSort(arr, m + 1, r)
            return merge(arr, l, m, r)

        return MergeSort(nums, 0, len(nums) - 1)