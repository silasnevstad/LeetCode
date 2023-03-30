class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        jumps_remaining = 0
        
        for num in nums[:-1]:
            jumps_remaining = max(num, jumps_remaining - 1)


            if jumps_remaining == 0:
                return False
            
        return True
