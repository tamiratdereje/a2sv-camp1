# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def findDeepest(root = node, depth = 0):
            if not (root.left or root.right):
                return root , depth
            
            elif root.left and not root.right:
                return findDeepest(root.left, depth+1)
                
            elif root.right and not root.left:
                return findDeepest(root.right, depth+1)
            
            else:
                rootRight, depthRight = findDeepest(root.right, depth+1)
                rootLeft, depthLeft = findDeepest(root.left, depth+1)
                if depthLeft == depthRight:
                    return root, depthLeft
                
                elif depthLeft > depthRight:
                    return rootLeft, depthLeft
                elif depthLeft < depthRight:
                    return rootRight, depthRight
        
        ans, level = findDeepest()
        return ans
                    
            
            
        
