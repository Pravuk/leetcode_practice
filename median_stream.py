# Python code to implement the approach

from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.right_heap = []
        self.left_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.left_heap, -num)
        heappush(self.right_heap, -heappop(self.left_heap))
        if len(self.right_heap) > len(self.left_heap):
            heappush(self.left_heap, -heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.right_heap) != len(self.left_heap):
            return -self.left_heap[0]
        else:
            return (self.right_heap[0] - self.left_heap[0]) / 2


# Driver code
if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(10)
    mf.addNum(7)
    mf.addNum(12)
    m = mf.findMedian()
    pass
