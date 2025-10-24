# ...existing code...
from typing import Any, Iterable, List, Optional, Iterator

class Node:
    """Node for a singly linked list."""
    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    """Simple singly linked list with clear pointer-update comments.

    Methods:
        insert_at_end(value): append value to tail.
        delete_value(value): remove first node with matching value.
        traverse(): return list of node values in order.
    """
    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Initialize an empty list or populate from iterable (preserves order)."""
        self.head: Optional[Node] = None
        if iterable:
            for v in iterable:
                self.insert_at_end(v)

    def insert_at_end(self, value: Any) -> None:
        """Insert value at list tail.

        Pointer logic:
        - If list is empty, head must point to the new node.
        - Otherwise walk to current tail and set tail.next -> new_node,
          which links the old tail to the new tail.
        """
        new_node = Node(value)
        if self.head is None:
            # Empty list: head points to the sole node.
            self.head = new_node
            return

        # Find current tail (node whose next is None).
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        # curr is tail; link it to new_node by updating curr.next.
        curr.next = new_node  # pointer update: old_tail.next -> new_node

    def delete_value(self, value: Any) -> bool:
        """Delete the first node with the given value.

        Returns:
            True if a node was deleted, False if value not found.

        Pointer logic:
        - If the head contains the value, remove it by advancing head to head.next.
          This drops the old head from the list and makes the next node the new head.
        - Otherwise maintain prev and curr such that prev.next == curr.
          When curr.value matches, bypass curr by setting prev.next = curr.next,
          which links prev directly to curr's successor and removes curr from chain.
        """
        if self.head is None:
            return False

        # Special-case: head holds the target value.
        if self.head.value == value:
            # Advance head to the next node; old head is dropped.
            self.head = self.head.next  # pointer update: head -> old_head.next
            return True
        prev = self.head
        curr = self.head.next

        # Traverse with prev one step behind curr.
        while curr is not None:
            if curr.value == value:
                # Bypass curr by linking prev.next to curr.next.
                prev.next = curr.next  # pointer update: prev now points to curr's successor
                return True
            prev = curr
            curr = curr.next
        # Value not found.
        return False
    def traverse(self) -> List[Any]:
        """Return a list of node values from head to tail."""
        out: List[Any] = []
        curr = self.head
        while curr is not None:
            out.append(curr.value)
            curr = curr.next
        return out
    def __iter__(self) -> Iterator[Any]:
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.traverse()})"
if __name__ == "__main__":
    # Minimal demonstration / sanity checks
    ll = SinglyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    print("After inserts:", ll.traverse())        # -> [1, 2, 3]

    ll.delete_value(1)                            # delete head
    print("After deleting head (1):", ll.traverse())  # -> [2, 3]

    ll.delete_value(3)                            # delete tail
    print("After deleting tail (3):", ll.traverse())  # -> [2]

    deleted = ll.delete_value(42)                 # non-existent
    print("Deleted 42?", deleted, "List:", ll.traverse())  # -> False, [2]
# ...existing code...