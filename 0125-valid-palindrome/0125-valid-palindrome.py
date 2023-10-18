class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Version 1: filter, lower, reverse
        # Keep lower alphanum characters
        # clean_string = "".join([character.lower() for character in s if character.isalnum()])
        # Compare to reversed string
        # return clean_string == clean_string[::-1]

        # Version 2: two pointers

        start = 0
        end = len(s) - 1

        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True 