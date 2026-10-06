class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       min_length= float("inf");
       curr_sum=0
       left =0
       for i in range(len(nums)):
        curr_sum+=nums[i];
        while(curr_sum>= target):
            min_length= min(min_length, i -left+1)
            curr_sum-=nums[left]
            left+=1
       return min_length if min_length != float('inf') else 0


        