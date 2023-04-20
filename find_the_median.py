def findMedian(arr):
    arr.sort()
    n = len(arr)
    median = arr[n // 2]
    return median