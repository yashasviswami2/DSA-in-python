# import time
# import numpy as np



# def merge_sort(arr):
#     # Merge Sort algorithm to sort the array
#     if len(arr) > 1:
#         mid = len(arr) // 2  # Find the middle of the array
#         left_half = arr[:mid]  # Divide the array elements into two halves
#         right_half = arr[mid:]

#         merge_sort(left_half)  # Sort the first half
#         merge_sort(right_half)  # Sort the second half


#         i = j = k = 0

#      # Copy data to temp arrays L[] and R[]
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
    
#         # Checking if any element was left
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
    
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1



# def measure_time_merge_sort():
#     # Measure the time taken for merge sort for different input sizes
#     input_sizes = [10**i for i in range(1, 7)]  # Input sizes: 10, 100, 1000, ..., 10^6
    
#     for size in input_sizes:
#         arr = np.arange(size, 0, -1)  # Create an array from size to 1
#         start_time = time.time_ns()  # Get the start time in nanoseconds
#         merge_sort(arr)  # Sort the array using merge sort
#         end_time = time.time_ns()  # Get the end time in nanoseconds
#         print(f"Time taken to sort an array of size {size}: {(end_time - start_time)} nanoseconds")

# if __name__ == "__main__":
#     measure_time_merge_sort()
