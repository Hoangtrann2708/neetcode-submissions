import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        convert = [0]*len(points)
        for i in range(len(points)):
            dis = math.sqrt((points[i][0] - 0)**2 + (points[i][1]-0)**2)
            convert[i]= dis,points[i]

        
        heapq.heapify(convert)
        output = [0]* k 

        for j in range (k): 
            output[j]= heapq.heappop(convert)[1]
        return output 
            
            



        