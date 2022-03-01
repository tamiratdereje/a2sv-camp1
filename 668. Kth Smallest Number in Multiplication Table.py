class Solution(object):
    
    def countLessNum(self,r,c,num):
        count=0
        for row in range(1,r+1):
            la =num//row
            count+=min(la, c)
            
        return count
    
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        
        
        first = 1
        last = n*m
        
        while first < last:
            mid = first + (last-first)//2
            
            if self.countLessNum(m,n,mid) < k:
                first = mid + 1
            else:
                last = mid
        
        return first
