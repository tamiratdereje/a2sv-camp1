class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.li = []
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            self.li.append(node.val)
            traverse(node.right)
 
        traverse(root)
        
        first , second = 0, 1
        point1 = self.li[0]
        while second < len(self.li):
            if self.li[first] > self.li[second]:
                print(self.li[first], "one", self.li[second])
                point1 = self.li[first]
                point2 = self.li[second]
                second += 1
                while second < len(self.li):
                    if self.li[second ] < point2 :
                        point2 = self.li[second]
                    second += 1
                break
            else:
                first += 1
                second += 1

        def swap(node):
            if node:
                if node.val == point1:
                    node.val = point2
                elif node.val == point2:
                    node.val = point1
                swap(node.left)
                swap(node.right)
            return
        swap(root)

