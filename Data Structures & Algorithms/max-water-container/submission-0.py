class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left =0;
        right = len(heights) -1
        while(left<right):
            usableHeight = min(heights[left], heights[right])
            width = right - left;
            currentSize = width*usableHeight;
            if currentSize > max:
                max=currentSize
            if(heights[left] > heights[right]):
                right-=1
            else:
                left+=1
        return max;


    

        