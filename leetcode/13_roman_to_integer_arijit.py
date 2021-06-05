class Solution:
    def romanToInt(self, s: str) -> int:
        l = []
        for i in s:
            l.append(i)
        length = len(l)
        prev = ''
        num = 0
        for j in range(length):
            if l[j] == 'I':
                if j != length - 1:
                    if l[j+1] == 'V':
                        num = num + 4
                    elif l[j+1] == 'X':
                        num = num + 9
                    else:
                        num = num + 1
                else:
                    num = num + 1
            elif l[j] == 'V':
                if prev == 'I':
                    None               
                else:
                    num = num + 5
            elif l[j] == 'X':
                if j != length - 1:
                    if l[j+1] == 'L' and j != length - 1:
                        num = num + 40
                    elif l[j+1] == 'C':
                        num = num + 90
                    elif prev == 'I':
                        None
                    else:
                        num = num + 10
                else:
                    if prev == 'I':
                        None
                    else:
                        num = num + 10
            elif l[j] == 'L':
                if prev == 'X':
                    None
                else:
                    num = num + 50
            elif l[j] == 'C':
                if j != length - 1:
                    if l[j+1] == 'D' and j != length - 1:
                        num = num + 400
                    elif l[j+1] == 'M':
                        num = num + 900
                    elif prev == 'X':
                        None
                    else:
                        num = num + 100
                else:
                    if prev == 'X':
                        None
                    else:    
                        num = num + 100
            elif l[j] == 'D':
                if prev == 'C':
                    None
                else:
                    num = num + 500
            elif l[j] == 'M':
                if prev == 'C':
                    None
                else:
                    num = num + 1000
            else:
                None
            prev = l[j]
        return num