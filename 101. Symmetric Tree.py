class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # palindrome = False
        queue = collections.deque()
        self.layer = 1
        queue.append([root,1])
        li = []
        palindrome = True
        while queue:
            current, level = queue.popleft()
            if current.left != None:    
                queue.append([current.left, level+1])
            if current.right != None:
                queue.append([current.right, level+1])
            if level == self.layer:
                li.append(current.left.val if current.left != None else None)
                li.append(current.right.val if current.right != None else None)
            if level > self.layer:
                self.layer = level
                if li == li[::-1]:
                    palindrome = True
                    li = []
                    li.append(current.left.val if current.left != None else None)
                    li.append(current.right.val if current.right != None else None)
                else:
                    return False 
        return palindrome
