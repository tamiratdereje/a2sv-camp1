class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
 
        self.times = times
        self.persons = persons
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        dicti = {}
        winner = []
        higher = self.persons[0]
        
        for i in self.persons:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i] = 1
            
            if dicti[best]<=dicti[i]:
                higher=i

            winner.append(higher)
        
        first = 0
        last = len(self.times) - 1  
        while first <= last:
            mid = first + (last - first)//2
            if t == self.times[mid]:
                break                   
            elif t < self.times[mid]:
                last = mid - 1
                mid = first + (last - first)//2
            else:
                if mid == first:
                    if self.times[last]<=t:
                        first = mid+1
                        mid = first + (last - first)//2
                    else:
                        last = mid
                        mid = first + (last - first)//2
                else:
                    first = mid + 1
                    mid = first + (last - first)//2  
                    
        return winner[mid]
                
    # Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
