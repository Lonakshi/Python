
##136. Single Number
## https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        digit = nums[0]
        for i in range(1, len(nums)):
            digit = digit^ nums[i]
            
        
        return digit