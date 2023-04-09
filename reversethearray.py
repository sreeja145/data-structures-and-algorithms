arr = list(map(int, input().split()))
# print reverse list
# Method 1
"""arr=arr[::-1]
print(*arr) """


# Method 2

def reverseList(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end = end - 1


reverseList(arr, 0, len(arr) - 1)
print(*arr)

"""
Input:
1 2 3 4 

Output:
4 3 2 1
"""
