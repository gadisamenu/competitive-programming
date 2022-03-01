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
        employees.sort( key = lambda employe: employe.id)
        self.tot_imp = 0
        
        def locator(idn):
            left = 0
            right = len(employees)-1
            while left <= right:
                mdl = left + (right-left)//2
                
                if employees[mdl].id < idn:
                    left = mdl+1
                elif employees[mdl].id > idn:
                    right = mdl-1
                else:
                    return mdl
                
        def dfs(employee):
            self.tot_imp += employee.importance
            for ids in employee.subordinates:
                dfs(employees[locator(ids)])
            return self.tot_imp
        return dfs(employees[locator(id)])
                
                
                
            