from heapq import *
def kthSmallest(root,k):
        def postorderTraversal(root):
            ans=[]
            def postorder(root,ans):
                if not root:
                    return ans
                else:
                    if root.left is not None:
                        postorder(root.left,ans)
                    if root.right is not None:
                        postorder(root.right,ans)
                    ans.append(root.val)    
                    return ans    
            return postorder(root,ans)     
        result=postorderTraversal(root)
        heap=[]
        heapify(heap)
        for i in result:
            heappush(heap,i*-1)
            if len(heap)>k:
                heappop(heap) 
        return  heap[0]*-1