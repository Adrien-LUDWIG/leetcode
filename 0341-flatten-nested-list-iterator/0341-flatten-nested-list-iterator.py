# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

def flatten(nestedIterator):
    flattenList = []

    for element in nestedIterator:
        if element.isInteger():
            flattenList.append(element.getInteger())
        else:
            flattenList += flatten(element.getList())
    
    return flattenList

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatten_list = flatten(nestedList)
        self.flatten_list.reverse()

    def next(self):
        """
        :rtype: int
        """
        return self.flatten_list.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.flatten_list)

        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())