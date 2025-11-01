# import time

# def bubble_sort(arr):

#     # Bubble Sort algorithm to sort the array
#     n = len(arr)
#     for i in range(n):
#         # Traverse the array from 0 to n-i-1
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def measure_time_bubble_sort():
#     # Measure the time taken for bubble sort for different input sizes
#     input_sizes = [10**i for i in range(1, 7)]  # Input sizes: 10, 100, 1000, ..., 10^6
    
#     for size in input_sizes:
#         arr = np.arange(size, 0, -1)  # Create an array from size to 1
#         arr = list(range(size, 0, -1))  # Create a list from size to 1 without numpy
#         bubble_sort(arr)  # Sort the array using bubble sort
#         end_time = time.time_ns()  # Get the end time in nanoseconds
#         print(f"Time taken to sort an array of size {size}: {end_time - start_time} nanoseconds")

# measure_time_bubble_sort()