class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,v in enumerate(nums):
            c = target - v
            if c in values:
                return [values[c],i]
            else:
                values[v] = i
        return []