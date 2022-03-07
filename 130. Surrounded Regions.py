class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
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
                    if grid[new_row][new_col] == "O":
                        visited.add((new_row, new_col))
                        findIsland(grid,new_row, new_col,visited)
                                            
            if self.surrounded:   
                self.li.append([row, col])
        
        if len(grid) == 1 and grid[0][0] == "O":
            return grid
        m = len(grid)
        n = len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                self.surrounded = True
                self.li = []
                if grid[i][j] == "O" and (i,j) not in visited:
                    visited.add((i,j))
                    findIsland(grid, i , j, visited)
                    if self.surrounded:
                        for a, b in self.li:
                            grid[a][b] = "X"
                            
        return grid
        
         
