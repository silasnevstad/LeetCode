class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)): # does idea just faster 
            return False
        else:
            return True
        # return len(set(nums))!=len(nums)
