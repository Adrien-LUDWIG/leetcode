MODULO = int(1e9) + 7

MEMO = [[1] * 10]

MOVES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}

class Solution:
    def knightDialer(self, n: int) -> int:
        k = len(MEMO)

        if k >= n:
            return sum(MEMO[n-1]) % MODULO

        for i in range(k, n):
            MEMO.append([])
            for cell in MOVES:
                MEMO[i].append(sum([MEMO[i-1][next_cell] for next_cell in MOVES[cell]]) % MODULO)
            
        return sum(MEMO[n-1]) % MODULO



        