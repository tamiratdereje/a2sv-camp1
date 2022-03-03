# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def findSum(node, parent, grandy):
            if node == None:
                return 0 
            if grandy:
                self.ans += node.val
            grandy = parent
            if node.val %2 == 0:
                parent = True
            else:
                parent = False

            findSum(node.left,parent, grandy)
            findSum(node.right,parent, grandy)
            
               
        findSum(root, False,False)
        return self.ans
