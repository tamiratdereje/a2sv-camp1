class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = {}
        def findMinCost(cost, inx):
            if inx in memory:
                return memory[inx]
            if inx > len(cost) - 1:
                return 0   
            memory[inx] = cost[inx] + min(findMinCost(cost,inx+1), findMinCost(cost,inx+2))
            return memory[inx]
        return min(findMinCost(cost, 0), findMinCost(cost, 1))
            
        

        

        
