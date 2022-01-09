import math

class Solution(object):
    def guessNumber(self, n):
        start, end = 1, n
        
        while start <= end:
            mid = (start + end)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                start = mid + 1
            else:
                end = mid
