class Solution:
    def isValid(self,n,arr,visited,index):
        return 0<=index<n and (index,arr[index]) not in visited
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]  == 0:
            return True
        queue = collections.deque()
        self.layer = 1
        visited = set()
        visited.add((start,arr[start]))
        queue.append((start,arr[start]))    
        while queue:
            index, val = queue.popleft()
            left = index - arr[index]
            right = index + arr[index]
            
            if self.isValid(len(arr),arr,visited,left):
                queue.append([left, arr[left]])
                visited.add((left, arr[left]))
                if arr[left] == 0:
                    return True
            if self.isValid(len(arr),arr,visited,right):
                queue.append([right, arr[right]])
                visited.add((right, arr[right]))
                if arr[right] == 0:
                    return True
        
        return False
