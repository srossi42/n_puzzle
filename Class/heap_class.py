import heapq

class Heap(object):

    def __init__(self):
        self._heap = []

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        if self._heap:
            item = heapq.heappop(self._heap)[1]
            return item

    def len(self):
        return len(self._heap)