# BST IMPLEMENTATION

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: No child
            if not node.left and not node.right:
                return None

            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: Two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

# GRAPH IMPLEMENTATION

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]

        print("BFS:", end=" ")

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor, _ in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)

            for neighbor, _ in self.graph.get(start, []):
                self.dfs(neighbor, visited)

# HASH TABLE IMPLEMENTATION

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)

# MAIN FUNCTION

def main():
    print("\n===== BST OPERATIONS =====")
    bst = BST()

    values = [55, 25, 75, 15, 35, 65, 85]
    for v in values:
        bst.insert(v)

    print("Inorder:", bst.inorder())
    print()
    print("Search 15:", bst.search(15))
    print("Search 100:", bst.search(100))
    print()
    bst.delete(15)
    print("After deleting 15:", bst.inorder())

    # Create one-child case
    bst.insert(68)
    bst.delete(65)
    print("After deleting 65:", bst.inorder())

    # Delete node with two children
    bst.delete(25)
    print("After deleting 25:", bst.inorder())

    print("\n===== GRAPH =====")
    g = Graph()

    edges = [
        ('A','B',5), ('A','C',3),
        ('B','D',6), ('B','E',2),
        ('C','E',4), ('C','F',7),
        ('E','D',1), ('D','F',8),
        ('E','F',9)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    g.print_graph()
    g.bfs('A')

    print("DFS:", end=" ")
    g.dfs('A')
    print()

    print("\n===== HASH TABLE =====")
    ht = HashTable(5)

    keys = [11, 16, 21, 6, 26]
    for k in keys:
        ht.insert(k, k * 5)

    ht.display()
    print()
    print("Get 11:", ht.get(11))
    print("Get 16:", ht.get(16))
    print("Get 6:", ht.get(6))
    print()
    ht.delete(16)
    print("After deleting 16:")
    ht.display()

if __name__ == "__main__":
    main()