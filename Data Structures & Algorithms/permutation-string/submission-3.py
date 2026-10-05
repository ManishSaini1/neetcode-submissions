from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length= len(s2)
        if s1_length > s2_length:
            return False
        left =0
        right=s1_length -1
        while left <=  (s2_length - s1_length):
            newString= s2[left:right+1]
            # print(newString)
            ans = not Counter(s1)-  Counter(newString)
            left+=1
            right+=1
            if ans:
                return True
        return False


        