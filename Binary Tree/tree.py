class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node: {self.val}, {self.left}, {self.right}>'    

class Binary_tree(object):
    def __init__(self):
        self.parent = None

    def construct(self, data):
        q = []
        if not len(data):
            return
        p_node = Node(data[0])
        q.append((p_node, 0))
        while len(q):
            node, index = q.pop(0)
            if index == 0:
                self.parent = node
            left_index = (2 * index) + 1
            right_index = (2 * index) + 2
            if left_index < len(data) and data[left_index]:
                left_node = Node(data[left_index])
                node.left = left_node
                q.append((left_node, left_index))
            else:
                node.left = None    
            if right_index < len(data) and data[right_index]:
                right_node = Node(data[right_index])
                node.right = right_node
                q.append((right_node, right_index))
            else:
                node.right = None        

    def display(self, d = 0, node = None):
        if not node:
            node = self.parent
        for i in range(0, d + 1):
            print(" ", end="")
        if d > 0:
            print("|_", end="")
        print(node.val)
        if node.left:
            self.display(d + 1, node.left)  
        if node.right:
            self.display(d + 1, node.right)  
                  
if __name__ == "__main__":
    tree_data = [50, 17, 65, 14, 20, 64, 100, None, 16, None, None, 19, 30]
    tree = Binary_tree()
    tree.construct(tree_data)
    tree.display()
