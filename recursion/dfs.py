from tree.tree import Node
"""
           a
         /   \
        b     c
       / \   /  \
      d   e f    g
"""

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
b.left = d
b.right = e
a.right = c
c.left = f
c.right = g


def dfs_rec(node, data = []):
    if node is None:
        return []
    ## data += str(node.data)
    data += [node.data]
    dfs_rec(node.left)
    dfs_rec(node.right)
    return data

"""        cur = stack.pop()
        if cur:
            temp.append(cur)
            if cur.data == data:
                ways.append(temp)
            stack.append(cur.right)
            stack.append(cur.left)"""


def dfs_stack(node):
    stack = [node]
    result = []
    while len(stack) > 0:
        cur = stack.pop()
        result.append(cur.data)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return result


#print(dfs_stack(a), dfs_rec(a))


# can used to find node but cant find path

is_present = False


def search_node_dfs(root, data):
    global is_present
    if root is None:
        return False
    # print(root)
    if root.data == data:
        is_present = True
        return is_present #line break if we got a match else search continues

    search_node_dfs(root.left, data)
    search_node_dfs(root.right, data)
    return is_present


temp = []
ways = []


def find_single_shortest_path(root, data):
    global ways, temp
    if root is None:
        print(temp)
        temp = []
        return
    print(root)
    temp.append(root.data)
    if root.data == data:
        ways.append(temp)
        temp = []
        return
    find_single_shortest_path(root.left, data)
    find_single_shortest_path(root.right, data)
    return ways

#error print(find_single_shortest_path(a, 'c'))


def leaf_node(node):
    if node.left is None and node.right is None:
        return True



def find_all_path_recursion(node, path=[]):
    if node is None:
        return
    path.append(node.data)
    if leaf_node(node):
        print(path)
        ways.append(path)

    find_all_path_recursion(node.left, path)
    find_all_path_recursion(node.right, path)
    path.pop()


find_all_path_recursion(a)



temp = []
ways = []
def print_all_path(node):
    global temp
    if not node:
        return
    print(node.data)
    temp.append(node.data)

    if leaf_node(node):
        print(temp)
        temp.pop()

    print(leaf_node(node))
    print_all_path(node.left)
    print_all_path(node.right)




