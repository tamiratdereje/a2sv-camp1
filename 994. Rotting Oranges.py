class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(grid,visited,row, col, m, n):
            
            return (0<=row<m) and (0<=col<n) and ((row, col) not in visited) and (grid[row][col] != 0)
            
        def findMinute(grid):
                      
        
            m = len(grid)
            n = len(grid[0])
            visited = set()
            queue = collections.deque()
            ans = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        queue.append([i,j,0])
                        visited.add((i,j))
                    if grid[i][j] != 1:
                        ans+=1

            if ans == m*n:
                return True
                        
            self.layer = 0
            while queue:
                
                direction = [[0,1],[1,0],[0,-1],[-1,0]]
                row,col,level = queue.popleft()
                rotten = False
                for dr in direction:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if isValid(grid,visited,new_row,new_col, m, n):
                        queue.append([new_row, new_col, level + 1])
                        visited.add((new_row, new_col))
                        grid[new_row][new_col]  = 2
                        rotten = True
                # print(level, " level ", self.layer, " layer")
                if level > self.layer and rotten == True:
                    # print(queue)
                    self.counta+=1
                    self.layer+=1
        
        self.counta = 1
        sm = findMinute(grid)
        if sm:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return self.counta
    
