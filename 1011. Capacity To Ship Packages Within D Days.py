class Solution(object):
    def possible(self,capacity, weights, days):
        currentWeight = 0
        currentDay = 1
        for weight in weights: 
            if weight > capacity:
                return False
            currentWeight += weight
            if currentWeight > capacity:
                currentWeight = weight
                currentDay+=1
                
        if currentDay <= days:
            return True
        else:
            return False
        
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        mini = weights[0]
        self.maxCapacity = mini
        for i in range(1,len(weights)):
            self.maxCapacity+=weights[i]
            if weights[i] < mini:
                mini = weights[i]   
        if len(weights) == 1:
            return weights[0]
            
        first = mini
        last = self.maxCapacity
        ans = -1
        while first <= last:
            mid  = first + (last - first)//2
            if self.possible(mid, weights, days):      
                last = mid - 1
                ans = mid
            else:                
                first = mid + 1           
        return ans   
    
    
    
