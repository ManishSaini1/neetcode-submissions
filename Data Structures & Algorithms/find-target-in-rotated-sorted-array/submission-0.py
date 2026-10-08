from typing import List

class Solution:
    def binarySearch(self, arr: List[int], target: int, low: int, high: int) -> int:
        # Fixed condition to <= to ensure the last element is checked
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        # Step 1: Find the pivot (index of the smallest element)
        low = 0
        high = len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            # Compare mid with high to find the rotation point safely
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
                
        pivot = low

        # Step 2: Determine which half of the array to search
        if pivot == 0:
            # The array is not rotated at all
            return self.binarySearch(arr, target, 0, len(arr) - 1)
        elif target >= arr[0] and target <= arr[pivot - 1]:
            # Target falls within the left sorted portion
            return self.binarySearch(arr, target, 0, pivot - 1)
        else:
            # Target falls within the right sorted portion
            return self.binarySearch(arr, target, pivot, len(arr) - 1)