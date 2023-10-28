class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec(n, currentVowel):
            if n == 0:
                return 1
            
            if (n, currentVowel) in memo:
                return memo[(n, currentVowel)]
            
            if currentVowel == 'a':
                result = rec(n-1, 'e')
            elif currentVowel == 'e':
                result = rec(n-1, 'a') + rec(n-1, 'i')
            elif currentVowel == 'i':
                result = rec(n-1, 'a') + rec(n-1, 'e') + rec(n-1, 'o') + rec(n-1, 'u')
            elif currentVowel == 'o':
                result = rec(n-1, 'i') + rec(n-1, 'u')
            else: # currentVowel == 'u'
                result = rec(n-1, 'a')

            memo[(n, currentVowel)] = result % modulo
            return result

        modulo = 10**9 + 7
        memo = {}
        result = 0
        
        for firstVowel in ('a', 'e', 'i', 'o', 'u'):
            result += rec(n-1, firstVowel)
        
        return result % modulo