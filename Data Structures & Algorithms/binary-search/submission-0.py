class Solution:

    def binarySearch(self,nums,  left, right, target):
        if(left > right):
            return -1
        mid = (left + right)//2
        if(nums[mid] == target):
            return mid
        if(nums[mid] < target):
            return self.binarySearch(nums,mid+1, right, target)
        if(nums[mid] > target):
            return self.binarySearch(nums,left, right-1, target)
        

    def search(self, nums: List[int], target: int) -> int:
        size= len(nums)
        return self.binarySearch(nums, 0, size -1, target)
        
        