from collections import deque
from typing import Any, Optional
import time

class ListQueue:
    """Queue implementation using Python list."""
    
    def __init__(self):
        self._items = []
    
    def enqueue(self, item: Any) -> None:
        """Add item to end of queue."""
        self._items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """Remove and return item from front of queue."""
        if self.is_empty():
            return None
        return self._items.pop(0)  # O(n) operation
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0

class DequeQueue:
    """Optimized queue implementation using collections.deque."""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item: Any) -> None:
        """Add item to end of queue."""
        self._items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """Remove and return item from front of queue."""
        if self.is_empty():
            return None
        return self._items.popleft()  # O(1) operation
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0

def performance_test(n: int = 100000):
    """Compare performance of both queue implementations."""
    list_queue = ListQueue()
    deque_queue = DequeQueue()
    
    # Test ListQueue
    start_time = time.time()
    for i in range(n):
        list_queue.enqueue(i)
    for _ in range(n):
        list_queue.dequeue()
    list_time = time.time() - start_time
    
    # Test DequeQueue
    start_time = time.time()
    for i in range(n):
        deque_queue.enqueue(i)
    for _ in range(n):
        deque_queue.dequeue()
    deque_time = time.time() - start_time
    
    print(f"\nPerformance comparison with {n} operations:")
    print(f"List-based queue time: {list_time:.4f} seconds")
    print(f"Deque-based queue time: {deque_time:.4f} seconds")
    print(f"Deque is {list_time/deque_time:.1f}x faster")

def test_functionality():
    """Test basic functionality of both implementations."""
    for QueueClass in [ListQueue, DequeQueue]:
        print(f"\nTesting {QueueClass.__name__}:")
        queue = QueueClass()
        
        print(f"Empty queue: {queue.is_empty()}")
        
        # Test enqueue
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(f"After enqueuing 1,2,3: not empty = {not queue.is_empty()}")
        
        # Test dequeue
        print(f"Dequeued: {queue.dequeue()}")  # Should print 1
        print(f"Dequeued: {queue.dequeue()}")  # Should print 2
        print(f"Dequeued: {queue.dequeue()}")  # Should print 3
        print(f"Empty queue: {queue.is_empty()}")

if __name__ == "__main__":
    test_functionality()
    performance_test()