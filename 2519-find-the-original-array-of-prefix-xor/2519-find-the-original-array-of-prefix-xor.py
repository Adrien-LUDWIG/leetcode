class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = []
        total = 0
        
        for i in range(len(pref)):
            arr.append(total ^ pref[i])
            total ^= arr[i]
        
        return arr