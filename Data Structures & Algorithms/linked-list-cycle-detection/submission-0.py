# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # As long as fast hasn't reached the end of the list
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            # Check for collision INSIDE the loop
            if slow == fast:
                return True
                
        # If the loop terminates, fast reached the end (no cycle)
        return False