# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def findBalanced(self,root):
        if not root:
            return 0
        left = self.findBalanced(root.left)
        if left == -1:
            return -1
        right= self.findBalanced(root.right)
        if right ==-1:
            return -1
        out= abs(right - left) > 1
        if out:
            return -1
        return 1 + max(left, right)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.findBalanced(root)!=-1
        