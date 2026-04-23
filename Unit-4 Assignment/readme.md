# Data Management Mini Toolkit (DMMT)

**Course:** Data Structure (ETCCDS202) 
**Unit-4:** Non-Linear and Advanced Data Structures  
**Student Name:** Shivansh Dahiya
**Roll No.:** 2501730145

---

## 1. Binary Search Tree (BST)
### Observations & Logic
**Inorder Traversal:** In a BST, the left subtree contains values smaller than the root, and the right subtree contains values larger.Visiting these in the order **Left -> Root -> Right** (Inorder) naturally retrieves data in sorted, non-decreasing order.
**Deletion Handling:** The implementation handles three critical cases:
    1. **Leaf Node:** Simply removed.
    2. **One Child:** The parent's pointer is updated to the child of the deleted node.
    3. **Two Children:** The node is replaced by its **Inorder Successor** (the smallest value in the right subtree) to maintain the BST property.

### Time Complexity
| Case | Time Complexity | Reason |
| :--- | :--- | :--- |
| **Average** | $O(\log n)$ | Each comparison eliminates half of the remaining tree. |
| **Worst** | $O(n)$ | Occurs when the tree becomes "skewed" (acting like a linked list). |

---

## 2. Graph Representation & Traversal
### Observations & Logic 
**Representation:** The graph is stored using an **Adjacency List**, which is memory-efficient for sparse graphs compared to a matrix.
**BFS (Breadth-First Search):** Uses a **Queue** to explore neighbors level-by-level.It is ideal for finding the shortest path in unweighted networks.
**DFS (Depth-First Search):** Uses **Recursion (Stack logic)** to go as deep as possible into a branch before backtracking.

### Real-World Use Cases
**BFS:** Peer-to-peer networks or finding the "shortest connection" on social media.
**DFS:** Detecting cycles in a circuit or solving puzzles (mazes) where every path must be explored to a dead end.

---

## 3. Hash Table with Separate Chaining
### Observations & Logic
**Collisions:** A collision occurs when different keys produce the same index via the hash function (e.g., $10 \pmod 5 = 0$ and $15 \pmod 5 = 0$)
**Separate Chaining:** To handle this, each "bucket" in the table stores a list (chain) of entries[cite: 177]. [cite_start]New colliding entries are simply appended to the list at that index
**Efficiency:** This ensures that even if a collision occurs, data is not lost and can still be retrieved by traversing the small list.

### Time Complexity
| Case | Time Complexity | Reason |
| :--- | :--- | :--- |
| **Average** | $O(1)$ | Direct access to the bucket index with a short chain. |
| **Worst** | $O(n)$ | Occurs if many keys hash to the exact same bucket. |

---

## 4. Conclusion
The DMMT demonstrates how non-linear structures provide efficient ways to manage data.BSTs provide ordered storage, Graphs map complex relationships, and Hash Tables offer near-instant lookups, forming the backbone of modern databases and routing systems.

## 5. References [cite: 184]
Unit-4 Course Material: Non-Linear & Advanced Data Structures.
Python Documentation for `collections.deque` and list management.
