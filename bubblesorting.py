
"""
It is the simplest sorting algorithm that works by swapping the adjacent elements if they are not in correct order
Not suitable for large data sets as its average and worst case time complexity is quite high.
"""


def bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = list(map(int, input().split()))
n = len(arr)
bubble_sort(arr,n)
print(*arr)

"""
INput: 1 4 6 7 2 4 6 7 8
output: 1 2 4 4 6 6 7 7 8
"""
"""
Time complexity: O(n^2)
Space complexity:O(1)
"""