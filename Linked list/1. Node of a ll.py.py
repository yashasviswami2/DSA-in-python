# Create a node for LL:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

print(id(first), (id(second), id(third)))
first.next = second
print(first.next.data)