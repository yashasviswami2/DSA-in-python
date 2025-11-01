class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLLFromList(lst):
    if not lst:
        return None
    head = Node(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" -> " if temp.next else "\n")
        temp = temp.next

head = createLLFromList([1,2,3,4,5])

print_LL(head)

def search_by_value(head,value):
    temp = head
    index = 0


    while temp != None :
        if(temp.data == value):
            return index
        temp =temp.next
        index+=1

    return "Not Found"

def search_by_value_recursive(head,value):
    pass

print("Searching ")
print(search_by_value(head,5))


        