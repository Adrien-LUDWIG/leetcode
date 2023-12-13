
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        # Minus 2 so we do not count "0b" from the binary string
        # Minus 1 because the exponent is one less than the lenght, ex:
        # "1" <=> 2**0, "10" <=> 2**1, ...
        k = len(bin(n)) - 2 - 1

        return 2 ** (k+1) - 1 - self.minimumOneBitOperations(n ^ 2**k)