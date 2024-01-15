class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins, losses = zip(*matches)
        winners = set(wins)
        loosers = set(losses)
        losses_count = Counter(losses)
        zero_loss = winners - loosers
        one_loss = [player for player in loosers if losses_count[player] == 1]
        return [sorted(zero_loss), sorted(one_loss)]