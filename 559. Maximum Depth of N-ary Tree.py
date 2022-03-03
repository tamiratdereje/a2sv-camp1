"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        
        def findDepth(currentDepth, node):
            
            self.maxDepth = currentDepth if currentDepth >= self.maxDepth else self.maxDepth
            
            for child in node.children:
                findDepth(currentDepth+1, child)
            
            return 

        if root is None:
            return 0
        currentDepth = 1
        self.maxDepth = 1
        findDepth(currentDepth, root)
        return self.maxDepth
    
    
