# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
           return None
        curr= head
        prev = None
        while(curr):
            next=curr.next
            curr.next= prev
            prev= curr
            curr= next
        return prev
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversedList= self.reverseList(head)
        if n == 1:
            return self.reverseList(reversedList.next)
        tempHead= reversedList
        start = 1
        currNext=None
        while(start < n -1):
            start+=1
            tempHead = tempHead.next
        next = tempHead.next
        if next:
            currNext= next.next
            tempHead.next=currNext

        return self.reverseList(reversedList)
        

        