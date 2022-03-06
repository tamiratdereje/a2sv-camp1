class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValid(grid,visited,row, col, m, n):
            
            return (0<=row<m) and (0<=col<n) and ((row, col) not in visited) and (grid[row][col] == 1)
        
        def findIsland(grid,row, col ,visited):
            m = len(grid)
            n = len(grid[0])
            if not grid[row][col]: 
                return
            
            self.counta += 1
            
            direction = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr in direction:
                new_row, new_col = row + dr[0], col + dr[1]
                
                if isValid(grid,visited,new_row, new_col, m, n):
                    visited.add((new_row, new_col))
                    findIsland(grid,new_row, new_col,visited)

                    
        m = len(grid)
        n = len(grid[0])
        visited = set()
        maxi = 0
        for i in range(m):
            for j in range(n):
                self.counta = 0
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    findIsland(grid, i , j, visited)
                    if self.counta >= maxi:
                        maxi = self.counta
                            
        return maxi
        
         
