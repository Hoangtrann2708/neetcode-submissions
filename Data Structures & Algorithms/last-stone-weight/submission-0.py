import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) 
        while len(stones) >=2 :
            first = heapq.heappop_max(stones)
            second =heapq.heappop_max(stones)
            if first>second:
                back = first - second
                heapq.heappush_max(stones,back)
            elif first<second:
                back = second - first
                heapq.heappush_max(stones,back)
        return stones[0] if len(stones)==1 else 0




    