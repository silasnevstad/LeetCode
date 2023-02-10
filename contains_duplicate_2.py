class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(set(nums))==len(nums):
            return False
        i=0
        while i < len(nums):
            if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
                return True
            i+=1
