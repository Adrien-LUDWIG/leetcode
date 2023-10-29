from math import log
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        EPSILON = 0.1
        tries = minutesToTest // minutesToDie
        return int(log(buckets - EPSILON, tries + 1) + 1)