class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node: {self.val}, {self.left}, {self.right}>'    

class Binary_tree(object):
    def __init__(self):
        self.root = None

    def construct(self, data):
        nodes = []
        for val in data:
            if val:
                nodes.append(Node(val))
            else:
                nodes.append(None)    
        reversed = nodes[::-1]
        self.root = reversed.pop()
        for node in nodes:
            if node:
                if reversed:
                    node.left = reversed.pop()
                if reversed:    
                    node.right = reversed.pop()      


    def display(self, d = 0, node = None):
        if not node:
            node = self.root
        for i in range(0, d + 1):
            print(" ", end="")
        if d > 0:
            print("|_", end=" ")
        print(node.val)
        if node.left:
            self.display(d + 1, node.left)  
        if node.right:
            self.display(d + 1, node.right)  
       
                  
if __name__ == "__main__":
    tree_data = [1,2,3,None,None,4,None,None,5]
    tree_data = [1,None,2,None,3]
    tree = Binary_tree()
    tree.construct(tree_data)
    tree.display()
    print(tree.get_tree())
