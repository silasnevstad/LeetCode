class Solution(object):
    def runningSum(self, nums):
        lst = nums
        for i in range(1, len(lst)):
            lst[i] += lst[i - 1]
            
        return lst
