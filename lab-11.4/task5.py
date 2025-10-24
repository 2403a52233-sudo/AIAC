from collections import deque
from typing import Dict, List, Set, Hashable, Iterable, Optional
class Graph:
    """Graph using an adjacency-list representation.
    Nodes are hashable (e.g., int, str). By default the graph is undirected
    unless directed=True is passed to the constructor.
    """
    def __init__(self, edges: Optional[Iterable[tuple]] = None, directed: bool = False) -> None:
        self.adj: Dict[Hashable, List[Hashable]] = {}
        self.directed = directed
        if edges:
            for u, v in edges:
                self.add_edge(u, v)
    def add_edge(self, u: Hashable, v: Hashable) -> None:
        """Add an edge u->v (and v->u if undirected). Create nodes if missing."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        if not self.directed:
            # For undirected graphs also add the reverse connection
            self.adj[v].append(u)
    def bfs(self, start: Hashable) -> List[Hashable]:
        """Breadth-first search (level-order) from start.
        Returns nodes in the order they are visited. Uses a queue (FIFO).
        Comments:
        - Mark start as visited and enqueue it.
        - While queue not empty: dequeue node, record it, then enqueue
          each unvisited neighbor marking them visited immediately to avoid duplicates.
        """
        if start not in self.adj:
            return []
        visited: Set[Hashable] = {start}        # nodes we've seen
        order: List[Hashable] = []              # visitation order
        q = deque([start])                      # queue of nodes to process

        while q:
            node = q.popleft()                  # visit nodes in FIFO order -> level by level
            order.append(node)
            # Enqueue unvisited neighbors (mark visited when enqueued)
            for nbr in self.adj.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)            # mark as seen to prevent multiple enqueues
                    q.append(nbr)
        return order
    def dfs_iterative(self, start: Hashable) -> List[Hashable]:
        """Iterative depth-first search using an explicit stack (LIFO).
        Returns nodes in the order visited. Comments:
        - Push start on stack.
        - Pop a node, if not visited mark visited and push its neighbors.
        - To preserve a natural left-to-right neighbor order, push neighbors
          in reversed order so the first neighbor is processed first.
        """
        if start not in self.adj:
            return []
        visited: Set[Hashable] = set()
        order: List[Hashable] = []
        stack: List[Hashable] = [start]          # stack holds nodes to visit
        while stack:
            node = stack.pop()                  # LIFO -> dive deep before siblings
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            # Push neighbors reversed so left-most neighbor is visited first
            for nbr in reversed(self.adj.get(node, [])):
                if nbr not in visited:
                    stack.append(nbr)
        return order

    def dfs_recursive(self, start: Hashable) -> List[Hashable]:
        """Recursive depth-first search (wrapper).

        Returns nodes in preorder (visit node, then recurse on neighbors).
        Comments:
        - Simpler code but may hit recursion limits for very deep graphs.
        - Uses visited set to prevent infinite recursion on cycles.
        """
        if start not in self.adj:
            return []

        visited: Set[Hashable] = set()
        order: List[Hashable] = []

        def _dfs(node: Hashable) -> None:
            visited.add(node)
            order.append(node)
            for nbr in self.adj.get(node, []):
                if nbr not in visited:
                    _dfs(nbr)
        _dfs(start)
        return order
if __name__ == "__main__":
    # Small demo graph (undirected)
    # A - B - D
    # |   |
    # C - E
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "E")
    print("Adjacency list:", g.adj)
    print("BFS from A:", g.bfs("A"))                # level-order from A
    print("DFS iterative from A:", g.dfs_iterative("A"))  # depth-first using stack
    print("DFS recursive from A:", g.dfs_recursive("A"))  # depth-first using recursion