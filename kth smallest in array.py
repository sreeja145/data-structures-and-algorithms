""" find the kth smallest element in the given array"""
arr=list(map(int,input().split()))
k=int(input())
arr.sort()
print("kth smallest in array: ", arr[k-1])
"""
Input:
12 45 7 7 1 8 4
3
Output:
kth smallest in array:  7
"""