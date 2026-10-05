class Solution:
    def max_sum(self, root, sum):
        if not root:
            return 0
        curr_value = root.val
        left = 0                      # changed from float("-inf")
        right = 0                     # changed from float("-inf")
        if root.left:
            left = max(self.max_sum(root.left, root.left.val), 0)    # drop negative branches
        if root.right:
            right = max(self.max_sum(root.right, root.right.val), 0) # drop negative branches
        self.best = max(self.best, curr_value + left + right)        # record path bending here
        return curr_value + max(left, right)                         # return only one side upward

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        self.best = float("-inf")     # added: tracks the overall answer
        self.max_sum(root, root.val)
        return self.best              # return the tracked best