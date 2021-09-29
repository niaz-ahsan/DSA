class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node: {self.val}, {self.left}, {self.right}>'

class BST(object):
    def __init__(self):
        self.root = None

    def add_node(self, node, curr_root = None):
        if curr_root is None:
            curr_root = self.root
        if self.root is None:
            self.root = node
        else:
            if node.val < curr_root.val:
                if curr_root.left:
                    self.add_node(node, curr_root.left)
                else:
                    curr_root.left = node
            else:
                if curr_root.right:
                    self.add_node(node, curr_root.right)
                else:
                    curr_root.right = node  

    def search(self, val, curr_node = None):
        if curr_node is None:
            curr_node = self.root
        if val == curr_node.val:
            return True
        elif val < curr_node.val:
            if curr_node.left:
                return self.search(val, curr_node.left)
            else:
                return False
        else:
            if curr_node.right:
                return self.search(val, curr_node.right)
            else:
                return False                       

    # showing inorder so data are shown as sorted
    def display(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.display(node.left)
        print(node.val, end = " ")
        if node.right:
            self.display(node.right)          


if __name__ == "__main__":
    tree = BST()
    tree.add_node(Node(50))
    tree.add_node(Node(17))
    tree.add_node(Node(65))
    tree.add_node(Node(55))
    tree.add_node(Node(71))
    tree.add_node(Node(60))
    tree.add_node(Node(100))
    tree.display()
    print()
    print("60 exists in tree?", end=" ")
    print(tree.search(60))
    print("72 exists in tree?", end=" ")
    print(tree.search(72))