import math
class Solution:
    def get_current_rate(self,mid, piles):
        total_efforts=0
        for i in piles:
            total_efforts+= (i+mid -1)//mid
        # print(mid)
        # print(".    ..")
        # print(total_efforts)
        return total_efforts

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        max_element= max(piles)
        min_k= float("inf")
        
        while(start <= max_element):
            mid = (start + max_element)//2
            current_rate= self.get_current_rate(mid,piles)
            if(current_rate <= h):
                max_element= mid-1
            else:
                start = mid+1
        return start