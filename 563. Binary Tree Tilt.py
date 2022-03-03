# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        def findSum(node):
            if node == None:
                return 0 
            left = findSum(node.left)
            right = findSum(node.right)
            self.tilt += abs(left-right)
            return left + right + node.val       
        findSum(root)
        return self.tilt
