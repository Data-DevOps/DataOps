class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        l = []
        y = x
        z = x
        if x > 0:
            while (y > 0):
                l.append(x%10)
                y = y//10
            length = len(l)
            while (x > 0):
                num = num + (x%10) * (10 ** (length-1))  
                x = x//10
                length = length - 1
            if z == num:
                return True
            else:
                return False
        elif x == 0:
            return True
        else:
            return False  