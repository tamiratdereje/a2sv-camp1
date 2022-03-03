# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def findSum(node,targetSum, currentSum):
            
            if node.left!=None:
                findSum(node.left , targetSum , currentSum + node.left.val)
            
            if node.right!=None:
                findSum(node.right , targetSum , currentSum + node.right.val)
                
            if node.left==None and node.right == None:                 
                if currentSum == targetSum:
                    self.ans = True
                    return 
                return
        self.ans = False
        if root is None:
            return False
        currentSum = root.val
        findSum(root,targetSum, currentSum)
        return self.ans                    
            
