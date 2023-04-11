"""
divide and conquer algorithm, it picks an element as pivot and partition the array using picked pivot
"""
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sot(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sot(arr,low,pi-1)
        quick_sot(arr,pi+1,high)

arr=list(map(int,input().split()))
quick_sot(arr,0,len(arr)-1)
print(*arr)
