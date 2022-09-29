# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = []
        self.ind =  0
        def recr(nL):
            for i in range(len(nL)):
                
                if nL[i].isInteger(): self.flat.append(nL[i].getInteger())
                else: recr(nL[i].getList())
        recr(nestedList)
            
    def next(self) -> int:
        self.ind += 1
        return self.flat[self.ind-1]
    
    def hasNext(self) -> bool:
        return True if self.ind < len(self.flat) else False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())