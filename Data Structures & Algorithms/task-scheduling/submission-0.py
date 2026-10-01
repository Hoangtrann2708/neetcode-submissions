import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## A,A,A,B,C
        hashset = set()
        for c in tasks: 
            hashset.add(c) # A,B,C
        counts = [0]*26 # [0,0,0,0,....,0, 0]
        for i in tasks: 
            if i in hashset:
                counts[ord(i)- ord('A')]+=1
        ## counts {3,1,1,0,0,0,0,0,0,0,0,0}
        heap = []
        for c in counts:
            if c >0:
                heap.append(c)
        ## heap [3,1,1]
        heapq.heapify_max(heap)
        q=deque()
        time = 0
        while heap or q: 
            time +=1 
            if len(heap)>0:
                cnt =heapq.heappop_max(heap)-1
                if cnt>0:
                    q.append([cnt,time+n])
            if q and q[0][1]== time:
                item = q.popleft()
                heapq.heappush_max(heap,item[0])
        return time
        
        
            

        
        



        
        

        