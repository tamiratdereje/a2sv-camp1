class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        self.dic = {}
        self.triangle = triangle
        def minPath(row, col):
            if row == len(self.triangle)-1:
                return triangle[row][col]
            a = 0
            b = 0
            if (row+1, col) in self.dic:
                a = self.dic[(row+1, col)]
            else:            
                a = minPath(row+1, col)
            
            if (row+1, col+1) in self.dic:
                b = self.dic[(row+1, col+1)]
            else:
                b = minPath(row+1, col+1)
            
            self.dic[(row, col)] = triangle[row][col] + min(a,b)
            return triangle[row][col] +  min(a,b)          
        
        return minPath(0,0)
                
