class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def min_max_sub(arr, target):
            l, r = 0, len(arr) - 1
            if target > arr[-1] or target < arr[0]:
                return False
            
            while l <= r:
                m = l + (r - l) // 2
                if target > arr[m]:
                    l = m + 1
                elif target < arr[m]:
                    r = m - 1
                else:
                    return True     
            return False
        
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                return min_max_sub(matrix[mid], target)
        return False
