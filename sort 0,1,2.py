"""
sort the array containing 0,1,2 without using sorting algorithms
"""
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
mid=0
while mid<=high:
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        mid=mid+1
        low=low+1
    elif arr[mid]==1:
        mid=mid+1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high=high-1
print("after sorting: ",*arr)

"""
Input: 0 1 2 0 1 2 1 1 0
after sorting:  0 0 0 1 1 1 1 2 2
"""