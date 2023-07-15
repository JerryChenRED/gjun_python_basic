import heapq
import random


class MaxHeap:
    def __init__(self):
        self.minheap = list()

    def insert(self, data):  # O (logN)
        heapq.heappush(self.minheap, data)
        # heapq.heapify(self.maxheap)  # 小到大
        heapq._heapify_max(self.maxheap)

    def pop_max(self):  # O (logN)
        max_one = heapq.heappop(self.minheap)
        # heapq.heapify(self.maxheap)
        heapq._heapify_max(self.minheap)
        return max_one

    def peek_max(self):
        return self.minheap[0] if self.minheap else None


class MaxHeap:
    def __init__(self):
        self.maxheap = list()

    def insert(self, data):
        heapq.heappush(self.maxheap, data)
        # heapq.heapify(self.maxheap)  # 小到大
        heapq._heapify_max(self.maxheap)

    def pop_max(self):
        max_one = heapq.heappop(self.maxheap)
        # heapq.heapify(self.maxheap)
        heapq._heapify_max(self.maxheap)
        return max_one

    def peek_max(self):
        return self.maxheap[0] if self.maxheap else None


if __name__ == "__main__":
    insert_order = random.sample(range(1, 1000), 100)
    print("Insert Order:", insert_order)

    max_heap = MaxHeap()
    for item in insert_order:
        max_heap.insert(item)

    while max_heap.peek_max():
        print(max_heap.pop_max())
