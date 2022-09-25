class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        s = y[::-1]
        if y == s:
            return True 
        else: 
            return False 