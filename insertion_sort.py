"""
it divides the given array into sorted and unsorted arrays"""
def Insertion_sort(arr,n):
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=list(map(int,input().split()))
n=len(arr)
Insertion_sort(arr,n)
print(*arr)

"""
input: 23 49 8 7 6 2 3 45
output: 2 3 6 7 8 23 45 49
"""
"""
Time complexity:O(n^2)
space complexity:O(1)
"""