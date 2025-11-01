# Return a head to a newly created LL
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!= None):
        print(temp.data)
        temp = temp.next


def take_input():
    value = int(input("Enter the value of node:- "))
    head = None  
    temp = head

    while (value != -1):
        newNode = Node(value)

    
