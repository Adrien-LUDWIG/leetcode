class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = [pref[0]]
        
        for i in range(1, len(pref)):
            arr.append(pref[i-1] ^ pref[i])
        
        return arr