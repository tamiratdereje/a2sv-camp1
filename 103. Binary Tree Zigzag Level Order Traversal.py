# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = collections.deque()
        self.layer = 1
        queue.append([root,1])
        li = []
        avg = []
        
        avg.append([root.val])
        while queue:
            current, level = queue.popleft()
            if current.left != None:    
                queue.append([current.left, level+1])
            if current.right != None:
                queue.append([current.right, level+1])
            if level == self.layer:
                if current.left != None:
                    li.append(current.left.val)
                if current.right != None:    
                    li.append(current.right.val)
                    
            if level > self.layer:
                if level %2 == 0:
                    li = li[::-1]
                    avg.append(li)
                    count = 0
                    self.layer = level
                    li = []
                else:
                    avg.append(li)
                    count = 0
                    self.layer = level
                    li = []
                if current.left != None:
                    li.append(current.left.val)
                if current.right != None:    
                    li.append(current.right.val)
        return avg
        
