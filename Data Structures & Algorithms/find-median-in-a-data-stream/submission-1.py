class MedianFinder:

    def __init__(self):
        self.arr =[]
        
    def addNum(self, num: int) -> None:
        l,r = 0, len(self.arr)
        while l < r:
            mid = (l+r)//2
            if num > self.arr[mid]:
                l = mid +1
            else:
                r = mid
        self.arr.insert(l,num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n%2 == 1:
            return self.arr[n//2]
        return (self.arr[n//2-1]+ self.arr[n//2]) /2

        
        

    ## 1234 even => median = arr(n/2 -1 + n/2 )/2  
    ## 12345 odd => median = array (n//2) 5//2 = 2 