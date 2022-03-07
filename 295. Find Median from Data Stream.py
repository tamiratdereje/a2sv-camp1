class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
        

    def addNum(self, num: int) -> None:
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.min_heap,num)
            heapq.heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap,-num)
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        else:
            return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
