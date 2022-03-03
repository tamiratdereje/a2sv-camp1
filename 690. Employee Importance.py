"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.dic = {}
        for employee in employees:
            self.dic[employee.id] = employee
      
        def findImportance(employee):
            if employee.subordinates == None:
                return employee.importance
            
            for subord in employee.subordinates:
                a = findImportance(self.dic[subord])
                self.ans += a
            return employee.importance
        employee = self.dic[id] 
        self.ans = employee.importance  
        findImportance(employee)
        return self.ans
        
