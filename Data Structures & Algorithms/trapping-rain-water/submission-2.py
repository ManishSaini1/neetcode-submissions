class Solution:
    def trap(self, height: List[int]) -> int:
        size= len(height)
        prefix_max = [float('-inf')] * size
        suffix_max = [float('-inf')] * size
        curr_max =-1;
        for i in range(len(height)):
            prefix_max[i] = max(curr_max,height[i])
            curr_max = max(curr_max, height[i]);
        curr_max = -1;
        for i in reversed(range(len(height))):
            suffix_max[i] = max(curr_max,height[i])
            curr_max = max(curr_max, height[i]);
        # print(prefix_max)
        # print(suffix_max)
        total_trapped_water=0
        for i in range(len(height)):
            total_trapped_water+= min(prefix_max[i], suffix_max[i]) - height[i]
        return total_trapped_water;
            


        