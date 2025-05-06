class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return #node already exist
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
            
    def in_order_traversal(self):
        result = []

        if self.left:
            result += self.left.in_order_traversal()
        
        result.append(self.data)

        if self.right:
            result += self.right.in_order_traversal()

        return result
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = build_tree([12, 2, 32, 33, 34, 55])
    print(numbers.in_order_traversal())

    
