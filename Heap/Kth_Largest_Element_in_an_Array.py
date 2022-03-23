from heapq import *
def findKthLargest(nums,k):
    heap=[]
    heapify(heap)
    for i in nums:
        heappush(heap,i)
        if len(heap)>k:
            heappop(heap)
    return heap[0] 