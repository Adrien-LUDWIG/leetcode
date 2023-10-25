class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def rec(n, k):
            if n == 0:
                return 0
    
            new_k = k % 2**(n-1)
            return (rec(n-1, new_k) + (k != new_k)) % 2

        return rec(n-1, k-1)