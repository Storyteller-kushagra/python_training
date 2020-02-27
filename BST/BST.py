class Node:
    def __init__(self, value, left = None, right = None):
        self.value =  value
        self.left =  left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        self.root = self.__add(value, self.root)

    def __add(self, value, node):

        if node == None:
            node = Node(value)
        else:
            if node.value > value:
                node.left = self.__add(value, node.left)
            if node.value < value:
                node.right = self.__add(value, node.right)
        return node

    def contains(self, value):
        return self.__contains(value, self.root)

    def __contains(self, value, node):

        if node == None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.__contains(value, node.left)
        else:
            return self.__contains(value, node.right)

if __name__ == " __main__ ":

    tree = BST()

    tree.add(20)
    tree.add(10)
    tree.add(30)
    tree.add(13)

    print(tree.contains(13))