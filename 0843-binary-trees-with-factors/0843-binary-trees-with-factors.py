class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def dp(index):
            if index == 0:
                return 1
            
            value = arr[index]

            if value in memo:
                return memo[value]
            
            ans = 1

            other_index = 0
            while arr[other_index] * arr[other_index] <= value:
                other = arr[other_index]

                if value % other == 0:
                    quotient = value // other
                    if quotient == other:
                        ans += dp(other_index) ** 2
                    elif quotient in arr:
                        ans += dp(other_index) * dp(arr.index(quotient)) * 2

                other_index += 1

            memo[value] = ans
            return ans
    
        memo = {}
        result =  0
        arr.sort()

        for i in range(len(arr)):
            result += dp(i)

        return result % (int(1e9) + 7)