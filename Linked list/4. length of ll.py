# Make sure 'common.py' is in the same directory or update the path below if needed
# If 'common.py' is not in the same directory, update the path below accordingly
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Ensure 'common.py' is in the same directory as this script.
# If not, update the import statement below with the correct relative path.
# Try importing from the current directory; if it fails, provide a helpful error message.
try:
    from common import Node, take_input_better, print_LL
except ModuleNotFoundError:
    raise ImportError("Could not find 'common.py'. Please ensure 'common.py' is in the same directory as this script.")

def lenthOfLL(head):
    temp = head
    ans = 0

    while(temp!=None):
        temp = temp.next
        ans = ans + 1

    return ans


headOfLL = take_input_better()

length = lenthOfLL(headOfLL)
print(length)


def lengthOfLinkedListRecursive(head):
    if(head==None): # Base Case
        return 0
    
    recursionAnswer = lengthOfLinkedListRecursive(head.next)

    return 1 + recursionAnswer

length = lengthOfLinkedListRecursive(headOfLL)
print(length)