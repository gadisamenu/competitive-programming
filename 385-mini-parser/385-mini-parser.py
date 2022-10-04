# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[": return NestedInteger(int(s))
                
        def rec(ind,node):
            srt = ind
            while ind < len(s):
                if s[ind] == ",":
                    if srt != ind: node.add(NestedInteger(int(s[srt:ind])))
                    srt = ind +1
                    
                elif s[ind] == "[":
                    ni = NestedInteger()
                    node.add(ni)
                    ind = rec(ind+1,ni)
                    srt = ind + 1
                    
                elif s[ind] == "]":
                    if srt != ind: node.add(NestedInteger(int(s[srt:ind])))
                    return ind
                
                ind += 1
                    
                      
        root = NestedInteger()
        rec(1,root)
        
        return root
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        