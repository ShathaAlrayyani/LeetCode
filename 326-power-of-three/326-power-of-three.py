class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 3
        if n == 0:
            return False
        if n == 1:
            return True
        while x <= n:
            if x != n:
                x = x * 3
            if x == n:
                return True 
        return False