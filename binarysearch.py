""" works for only ascending sorted data"""
n=int(input())
arr=list(map(int,input().split()))
find_element=int(input())
start=0
end=n-1
is_found=0
while start<=end:
    mid=(start+end)//2
    if arr[mid]==find_element:
        print("element found at position "+str(mid))
        is_found=1
        break
    elif arr[mid]>find_element:
        end=mid-1
    else:
        start=mid+1

if is_found==0:
    print("element not found")

"""
Input:
8
1 7 9 12 14 16 17
4
Output:
element not found
Input:
7
2 3 4 5 7 8 9
5
Output:
element found at position 3

Time Complexity: O(logn)
Space complexity : O(1)
"""