class Node:
    def __init__(self, data):
        self.des = 'Node'
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "Node({})".format(self.data)

    def __repr__(self):
        return "Node({})".format(self.data)


class Root(Node):
    def __init__(self, data):
        super().__init__(data)
        self.des = 'Root node'


class Tree:
    def __init__(self, root_data):
        self.root = Root(root_data)
        self.child = []

    def add_child(self, node, child, left=False, right= False):
        if left:
            node.left = child
        if right:
            node.right = child
        self.child.append(node)

    def get_all_child(self):
        return self.child

    def get_root(self):
        return self.root

    def print_tree(self):
        pass

    def dfs(self):
        pass

    def bfs(self):
        pass

