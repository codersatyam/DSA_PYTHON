from heapq import *
def topKFrequent(nums,k):
    hash_map={}
    for i in nums:
        hash_map[i]=hash_map.get(i,0)+1
    heap=[]
    heapify(heap)
    for key,value in hash_map.items():
        heappush(heap,[value,key])
        if len(heap)>k:
            heappop(heap)
    ans=[]        
    for i in range(k):
        ans.append(heap[i][1])
    return ans