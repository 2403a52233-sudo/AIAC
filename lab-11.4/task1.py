from collections import deque
from typing import Any, Optional

class Stack:
    """A stack data structure implementation with list and deque options."""
    def __init__(self, use_deque: bool = False):
        """Initialize empty stack.
        Args:
            use_deque: If True, uses collections.deque instead of list
        """
        self._use_deque = use_deque
        self._items = deque() if use_deque else []
    
    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)
    def pop(self) -> Optional[Any]:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return None
        return self._items.pop()
    
    def peek(self) -> Optional[Any]:
        """Return the top item without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Return True if stack is empty, False otherwise."""
        return len(self._items) == 0
    
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
def test_stack():
    """Test both list-based and deque-based stack implementations."""
    stack = Stack()
    print("Testing list-based stack:")
    _run_stack_tests(stack)
    stack = Stack(use_deque=True)
    print("\nTesting deque-based stack:")
    _run_stack_tests(stack)
def _run_stack_tests(stack: Stack):
    """Run a series of stack operations to test functionality."""
    print(f"Empty stack: {stack.is_empty()}")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack after pushes: {len(stack)} items")
    print(f"Top item (peek): {stack.peek()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Items remaining: {len(stack)}")

if __name__ == "__main__":
    test_stack()
