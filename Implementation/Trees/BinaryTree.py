class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Tree Traversal

    # Inorder Transversal
    def inorderTransversal(self, root, transversed_node=[]):
        if root == None:
            return
        root.inorderTransversal(root.left)
        transversed_node.append(root.data)
        root.inorderTransversal(root.right)
        return transversed_node


    # PostOrder Transversal
    def postorderTransversal(self, root, transversed_node=[]):
        if root == None:
            return
        root.postorderTransversal(root.left)
        root.postorderTransversal(root.right)
        transversed_node.append(root.data)
        return transversed_node

    # PreOrder Transversal
    def preorderTransversal(self, root, transversed_node = []):
        if root == None:
            return

        transversed_node.append(root.data)
        root.preorderTransversal(root.left)
        root.preorderTransversal(root.right)
        return transversed_node






root = Node(40)
root.insert(30)
root.insert(25)
root.insert(35)
root.insert(50)
print(root.left.left.data)

print('###### --- InOrder')
print(root.inorderTransversal(root))

print('###### --- PreOrder')
print(root.preorderTransversal(root))

print('###### --- Post')
print(root.postorderTransversal(root))
