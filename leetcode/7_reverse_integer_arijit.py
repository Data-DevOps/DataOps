class Solution:
    def reverse(self, x: int) -> int:
        l = []
        num = 0
        if ((x >= ((2 ** 31)-1)) or (x <= -(2 ** 31))):
            return 0
        else: 
            if x > 0:
                while(x != 0):
                    l.append(x%10)
                    x = x//10
                length = len(l)
                for i in l:
                    num = num + i * (10 ** (length - 1))
                    length = length - 1
                if ((num >= ((2 ** 31)-1)) or (num <= -(2 ** 31))):
                    return 0
                else:
                    return num               
            else:
                x = x * (-1)
                while(x != 0):
                    l.append(x%10)
                    x = x//10
                length = len(l)
                for i in l:
                    num = num + i * (10 ** (length - 1))
                    length = length - 1
                if ((num >= ((2 ** 31)-1)) or (num <= -(2 ** 31))):
                    return 0
                else:
                    return num * (-1)  