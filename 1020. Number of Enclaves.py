class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def isValid(grid,visited,row, col, m, n):
            
            return (0<=row<m) and (0<=col<n) and ((row, col) not in visited)
        
        def findIsland(grid,row, col ,visited):
            m = len(grid)
            n = len(grid[0])
            if not grid[row][col]: 
                return

            direction = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr in direction:
                new_row, new_col = row + dr[0], col + dr[1]
                
                if isValid(grid,visited,new_row, new_col, m, n):
                    if row == 0 or row == m-1 or col == 0 or col == n-1:
                        self.surrounded = False
                    if grid[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        findIsland(grid,new_row, new_col,visited)
                                            
            if self.surrounded:   
                self.li.append([row, col])
        
        if len(grid) == 1 and grid[0][0] == 1:
            return grid
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        self.counta = 0
        for i in range(m):
            for j in range(n):
                self.surrounded = True
                self.li = []
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    findIsland(grid, i , j, visited)
                    if self.surrounded:
                        self.counta+=len(self.li)
                            
        return self.counta
        
        
        
