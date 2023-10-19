class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = list(s)
        t = list(t)

        index_s = 0
            
        for character in s:
            if character == "#":
                if index_s > 0:
                    index_s -= 1
            else:
                s[index_s] = character
                index_s += 1

        index_t = 0
            
        for character in t:
            if character == "#":
                if index_t > 0:
                    index_t -= 1
            else:
                t[index_t] = character
                index_t += 1

        return index_s == index_t and s[:index_s] == t[:index_t]
