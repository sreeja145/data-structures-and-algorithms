"""
it is a simple and efficient algorithm that works repeatedly by selecting
the smallest and largest element moving it to the sorted portion of the array or list of elements.
"""


def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


arr = list(map(int, input().split()))
n = len(arr)
selection_sort(arr, n)
print(*arr)

"""
Input:
23 4 5 12 3 0 87 2
Output:
0 2 3 4 5 12 23 87
"""
"""
Time Complexity:O(n^2)
Space Complexity:O(1)
"""