
def linear_search(arr, target):
    """
    Perform a linear search for the target in the given array.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """

    size = len(arr)
    for index in range(0,size):
        if (arr[index] == target):
            return index
    return -1

my_list = [10,23,45,21,15,77,11]
target = 777

result = linear_search(my_list, target)
print(result)