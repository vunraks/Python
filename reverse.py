class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def display(self, node):
        if node:
            self.display(node.left)
            print(node.value)
            self.display(node.right)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)
    
#tree reverse
    def display_reverse(self,node):
        if node:
            self.display_reverse(node.right)
            print(node.value)
            self.display_reverse(node.left) 


    def find_min(self, node):
        while node.left:
            node = node.left
        return node.value

    def delete(self, value):
        self.root=self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        
  
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            min_value = self.find_min(node.right)
            node.value = min_value
            node.right=self._delete_recursive(node.right, min_value)
        return node






tree=BinaryTree()
tree.insert(10)
tree.insert(6)
tree.insert(7)
tree.insert(4)
tree.insert(15)
tree.insert(14)
tree.insert(17)

print("Обратный порядок")
tree.display_reverse(tree.root)

tree.display(tree.root)

tree.delete(15)

tree.display(tree.root)
print(tree.search(20))
