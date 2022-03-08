class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        i = 0
        j = len(people)-1
        peopleIn = 0
        print(people)
        while i <= j :
            if i == j:
                i+=1
                j-=1
                peopleIn+=1
            elif people[i] == limit:
                peopleIn += 1
                i+=1
            elif people[j] == limit:
                peopleIn += 1
                j-=1
            
            elif people[i] + people[j] <= limit:
                i+=1
                j-=1
                peopleIn += 1
            elif people[i] + people[j] > limit:
                j-=1
                peopleIn += 1
            
                
        return peopleIn      
