class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        elements = dict()
        chars = ""
        final = []
        length = len(strs)
        
        for i in strs:
            elements[i] = len(i)
        
        min = elements[strs[0]]
        
        min_element = strs[0]
        
        for i in elements:
            if elements[i] < min:
                min = elements[i]
                min_element = i
            else:
                None
        index = 0 
        for i in min_element:
            inter = 0

            for j in strs:
                for k in range(len(j)):
                    if j[k] == i and k == index:
                        inter = inter + 1
                        
            if inter == length:
                chars = chars + i       
            else:
                break
            index = index + 1
        return chars