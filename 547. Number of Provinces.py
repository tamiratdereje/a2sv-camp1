class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        def dfs(isConnected, row ,i ):
            for j in range(len(row)):
                if (i,j) not in self.visited and isConnected[i][j] == 1:
                    self.visited.add((i,j))
                    self.visited.add((j,i))
                    dfs(isConnected , isConnected[j] , j)
            return 
        count = 0
        for i in range(len(isConnected)):
            if (i,i) not in self.visited and isConnected[i][i] == 1 :
                dfs(isConnected, isConnected[i] , i)
                count += 1
        return count
