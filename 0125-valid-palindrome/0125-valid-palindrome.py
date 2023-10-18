class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Keep lower alphanum characters
        clean_string = "".join([character.lower() for character in s if character.isalnum()])
        # Compare to reversed string
        return clean_string == clean_string[::-1]