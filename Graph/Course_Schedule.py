from collections import deque
def canFinish(numCourses,prerequisites):
        graph={}
        indegree={}
        for i in range(numCourses):
            graph[i]=[]
            indegree[i]=0
        for i in prerequisites:
            parent=i[0]
            child=i[1]
            graph[parent].append(child)
            indegree[child]+=1
        queue=deque()    
        for key,value in indegree.items():
            if value==0:
                queue.append(key)
        sorted_order=[]        
        while queue:
            ele=queue.popleft()
            sorted_order.append(ele)
            for i in graph[ele]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(sorted_order)==numCourses:
            return True
        return False
            
            
            
        