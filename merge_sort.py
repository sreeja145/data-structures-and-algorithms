"""
In merge sorting algorithm, the array s divided into smaller sub arrays ,
 sorting and merging them, merging the sorted subarrays together to form the final sorted array.
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                k = k + 1
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
                k = k + 1
        while i < len(l):
            arr[k] = l[i]
            k = k + 1
            i = i + 1
        while j < len(r):
            arr[k] = r[j]
            k = k + 1
            j = j + 1


arr = list(map(int, input().split()))
merge_sort(arr)
print(*arr)

"""
input:
23 1 45 4 90 1
output:
1 1 4 23 45 90
"""
"""
Time complexity:O(nlogn)
space complexity:O(1)
"""
