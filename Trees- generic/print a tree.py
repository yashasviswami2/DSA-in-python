class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1)

child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)    
root.children.append(child3)

# print(root.children[0].data)


def print_tree(root):
    if(root == None):
        return
    print(root.data)
    for eachChild in root.children:
        print_tree(eachChild)

print_tree(None)

def print_tree_detailed(root):
    if root is None:
        return
    print(f"Node: {root.data}, Children: {[child.data for child in root.children]}")
    for eachChild in root.children:
        print_tree_detailed(eachChild)