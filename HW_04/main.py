class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "red"

class RedBlackTree():

    COLOR_RED = "red"
    COLOR_BLACK = "black"

    def __init__(self):
        self.root = None

    def turn_right(self, my_node):
        child = my_node.left
        child_right = child.right
        child.right = my_node
        my_node.left = child_right
        return child
    
    def turn_left(self, my_node):
        child = my_node.right
        child_left = child.left
        child.left = my_node
        my_node.right = child_left
        return child

    def is_red(self, my_node):
        return my_node != None and my_node.color == RedBlackTree.COLOR_RED

    def change_colors(self, node1, node2):
        temp = node1.color
        node1.color = node2.color
        node2.color = temp

    def insert(self, data):
        node = None
        if self.root:
            node = self.balance(self.root, data)
            if not node:
                return False
        else:
            node = Node(data)
        self.root = node
        self.root.color = RedBlackTree.COLOR_BLACK
        return True

    def balance(self, my_node, data):
        if my_node == None:
            return Node(data)
        if my_node.data > data:
            my_node.left = self.balance(my_node.left, data)
        elif my_node.data < data:
            my_node.right = self.balance(my_node.right, data)
        else:
            return None
        return self.balanced(my_node)

    def balanced(self, my_node):
        if self.is_red(my_node.right) and not self.is_red(my_node.left):
            my_node = self.turn_left(my_node)
            self.change_colors(my_node, my_node.left)
        if self.is_red(my_node.left) and self.is_red(my_node.left.left):
            my_node = self.turn_right(my_node)
            self.change_colors(my_node, my_node.right)
        if self.is_red(my_node.left) and self.is_red(my_node.right):
            my_node.color = RedBlackTree.COLOR_RED
            my_node.left.color = RedBlackTree.COLOR_BLACK
            my_node.right.color = RedBlackTree.COLOR_BLACK
        return my_node

    def draw_tree(self,node, offset=0):
        if node is not None:
            self.draw_tree(node.right, offset + 4)
            print(' ' * offset + str(node.data) + ' (' + node.color + ')')
            self.draw_tree(node.left, offset + 4)

if __name__ == "__main__":

    node = RedBlackTree()
    print("-----------------------")
    node.insert(10)
    node.draw_tree(node.root)
    print("-----------------------")
    node.insert(20)
    node.draw_tree(node.root)
    print("-----------------------")
    node.insert(30)
    node.draw_tree(node.root)
    print("-----------------------")
    node.insert(40)
    node.draw_tree(node.root)
    print("-----------------------")
    node.insert(50)
    node.draw_tree(node.root)
    print("-----------------------")
    node.insert(25)
    node.draw_tree(node.root)
