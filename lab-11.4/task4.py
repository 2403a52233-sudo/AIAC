from typing import Optional, List, Generator, Any


class Node:
    """Node for a binary search tree.

    Attributes:
        value: Stored value.
        left: Left child node or None.
        right: Right child node or None.
    """

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class BinarySearchTree:
    """Simple binary search tree (BST).

    Methods:
        insert(value): Insert value into BST (duplicates ignored).
        search(value): Return True if value exists in BST, else False.
        inorder_traversal(): Return sorted list of values (left, root, right).
    """

    def __init__(self) -> None:
        """Create an empty BST."""
        self.root: Optional[Node] = None

    def insert(self, value: Any) -> None:
        """Insert value into the BST. Duplicates are ignored.

        Args:
            value: Value to insert.
        """
        new_node = Node(value)
        if self.root is None:
            # Empty tree: new node becomes root
            self.root = new_node
            return

        curr = self.root
        while True:
            if value == curr.value:
                # Duplicate: do nothing
                return
            if value < curr.value:
                # Go left if possible; otherwise attach new_node as left child
                if curr.left is None:
                    curr.left = new_node  # parent.left -> new_node
                    return
                curr = curr.left
            else:
                # value > curr.value: go right or attach as right child
                if curr.right is None:
                    curr.right = new_node  # parent.right -> new_node
                    return
                curr = curr.right
    def search(self, value: Any) -> bool:
        """Search for value in BST.

        Args:
            value: Value to search for.

        Returns:
            True if value found, False otherwise.
        """
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            curr = curr.left if value < curr.value else curr.right
        return False

    def inorder_traversal(self) -> List[Any]:
        """Return list of values from inorder traversal (sorted order).

        Returns:
            List of values in ascending order.
        """
        return list(self._inorder_generator(self.root))

    def _inorder_generator(self, node: Optional[Node]) -> Generator[Any, None, None]:
        """Generator helper for inorder traversal (yields left, node, right)."""
        if node is None:
            return
        yield from self._inorder_generator(node.left)
        yield node.value
        yield from self._inorder_generator(node.right)

    def __repr__(self) -> str:
        return f"BinarySearchTree({self.inorder_traversal()})"
if __name__ == "__main__":
    # Sample test: insert integers and verify inorder and search behavior.
    values = [7, 3, 9, 1, 5, 8, 10]
    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)
    # Inorder traversal should produce sorted values
    print("Inserted values:", values)
    print("Inorder traversal (sorted):", bst.inorder_traversal())  # -> [1, 3, 5, 7, 8, 9, 10]
    # Search tests: present vs absent
    present = 5
    absent = 6
    print(f"Search {present}: {bst.search(present)}")  # True
    print(f"Search {absent}: {bst.search(absent)}")    # False
